import copy
import json
import time
import asyncio
import anyio
import websockets.exceptions
from fastapi import Depends
from app import models, schemas, get_db
from sqlalchemy.orm import Session
from app.common.validation import get_password_hash, create_access_token, verify_password, TokenSchemas, \
    check_access_token, check_user
import pandas as pd


def data_import(db: Session, df: pd.DataFrame):
    car_data = df.iloc[:, 4:].copy()
    car_data.columns = car_data.columns.str.strip().str.replace('\n', '')
    car_data.replace([pd.NA, float('inf'), float('-inf')], None, inplace=True)
    result = {}
    grouped = car_data.groupby(df['table'])
    for table_value, group in grouped:
        result[str(table_value)] = {}
        for col in group.columns[2:]:
            result[str(table_value)][col] = dict(zip(group['name_en'], group[col]))
    res = {
        "car_base_info": "",
        "K&C": "",
        "other": "",
    }
    try:
        process_car_base_info(db, result['1'])
        res["car_base_info"] = "Success"
    except Exception as e:
        print(f"处理单一坐标系统时出错: {e}")
        res["car_base_info"] = e
    try:
        table_keys_mappings = [
            (["2", "14"], models.VerticalParallelARBConnected),
            (["3", "15"], models.VerticalParallelARBDisconnected),
            (["4", "16"], models.VerticalRollARBConnected),
            (["5", "17"], models.VerticalRollARBDisconnected),
            (["6", "18"], models.SteeringKinematicsPASOn),
            (["7", "19"], models.LateralParallelInPhase),
            (["8", "20"], models.LateralParallelOutOfPhase),
            (["9", "21"], models.LateralParallelThirtyMillMetersTrail),
            (["10", "22"], models.AligningTorqueParallel),
            (["11", "23"], models.AligningTorqueOpposite),
            (["12", "24"], models.LongitudinalAcceleration),
            (["13", "25"], models.LongitudinalBraking),
            (["26", "28"], models.Structural_Parts),
            (["27", "29"], models.Elastic_Parts)
            # 添加其他映射
        ]
        for keys, model_class in table_keys_mappings:
            process_vertical_parallel_data(result, db, keys, model_class)
        res["K&C"] = "Success"
    except Exception as e:
        print(f"处理单一坐标系统时出错: {e}")
        res["K&C"] = e
    try:
        table_keys_to_model_map = {
            "30": models.Brake_control,
            "31": models.Brake_execution,
            "32": models.Upward_turn,
            "33": models.Downward_turn,
            "34": models.Transmission,
            "35": models.Suspension,
        }
        process_single_coordinate_system(result, db, table_keys_to_model_map)
        res["other"] = "Success"
    except Exception as e:
        print(f"处理单一坐标系统时出错: {e}")
        res["other"] = e
    return res


def process_car_base_info(db: Session, car_data: dict):
    car_names = list(car_data.keys())
    existing_car_names = {name[0] for name in
                          db.query(models.CarBaseInfo.name).filter(models.CarBaseInfo.name.in_(car_names)).all()}

    new_records = []
    for car_name, car_base_info in car_data.items():
        if car_name in existing_car_names:
            continue

        car_base_info["name"] = car_name
        car_base_info["platform_id"] = {"T1X": 1, "T2X": 2, "E0X": 3, "M1X": 4, "Benchmark": 5}.get(
            car_base_info.get("platform_id"))
        car_base_info["car_type_id"] = {"SD": 1, "SUV": 2, "MPV": 3}.get(car_base_info.get("car_type_id"))
        new_records.append(models.CarBaseInfo(**car_base_info))

    if new_records:
        db.bulk_save_objects(new_records)
        db.commit()


def process_vertical_parallel_data(result, db, table_keys, model_class):
    if not (result.get(table_keys[0]) and result.get(table_keys[1])):
        return

    car_names_1 = set(result.get(table_keys[0]).keys())
    car_names_2 = set(result.get(table_keys[1]).keys())
    car_names = car_names_1.union(car_names_2)

    car_base_info_ids = db.query(models.CarBaseInfo.id, models.CarBaseInfo.name).filter(
        models.CarBaseInfo.name.in_(car_names)).all()
    car_name_to_id = {name: id_ for id_, name in car_base_info_ids}

    existing_records = db.query(model_class.car_base_info_id, model_class.coordinate_system).filter(
        model_class.car_base_info_id.in_(car_name_to_id.values())).all()
    existing_pairs = {(record.car_base_info_id, record.coordinate_system) for record in existing_records}

    new_records = []
    for idx, table_data in enumerate([result.get(table_keys[0]), result.get(table_keys[1])]):
        for car_name, data in table_data.items():
            car_base_info_id = car_name_to_id.get(car_name)
            if car_base_info_id and (car_base_info_id, idx) not in existing_pairs:
                data.update({"car_base_info_id": car_base_info_id, "coordinate_system": idx})
                new_records.append(model_class(**data))

    if new_records:
        db.bulk_save_objects(new_records)
        db.commit()


def process_single_coordinate_system(result, db, table_keys_to_model_map):
    for table_key, model_class in table_keys_to_model_map.items():
        if not result.get(table_key):
            continue

        car_names = result.get(table_key).keys()
        car_base_info_ids = db.query(models.CarBaseInfo.id, models.CarBaseInfo.name).filter(
            models.CarBaseInfo.name.in_(car_names)).all()
        car_name_to_id = {name: id_ for id_, name in car_base_info_ids}

        existing_records = db.query(model_class.car_base_info_id).filter(
            model_class.car_base_info_id.in_(car_name_to_id.values()), model_class.coordinate_system == 0).all()
        existing_pairs = {record.car_base_info_id for record in existing_records}

        new_records = []
        for car_name, data in result.get(table_key).items():
            car_base_info_id = car_name_to_id.get(car_name)
            if car_base_info_id and car_base_info_id not in existing_pairs:
                data.update({"car_base_info_id": car_base_info_id, "coordinate_system": 0})
                new_records.append(model_class(**data))

        if new_records:
            db.bulk_save_objects(new_records)
            db.commit()
