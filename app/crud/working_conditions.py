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
from configs.setting import config


def get_working_conditions(db: Session):
    result: [models.WorkingConditions] = db.query(models.WorkingConditions).all()
    return result


def get_working_conditions_detail(item: schemas.WorkingConditions, db: Session):
    working_conditions_table_obj_dic = {
        "1": models.VerticalParallelARBConnected,
        "2": models.VerticalParallelARBDisconnected,
        "3": models.VerticalRollARBConnected,
        "4": models.VerticalRollARBDisconnected,
        "5": models.SteeringKinematicsPASOn,
        "6": models.LateralParallelInPhase,
        "7": models.LateralParallelOutOfPhase,
        "8": models.LateralParallelThirtyMillMetersTrail,
        "9": models.AligningTorqueParallel,
        "10": models.AligningTorqueOpposite,
        "11": models.LongitudinalAcceleration,
        "12": models.LongitudinalBraking,
    }
    table_obj_dic = {}
    table_obj_date_dic = {}
    for working_conditions_id in item.working_conditions_list:
        res: [models.WorkingConditions] = db.query(models.WorkingConditions).filter(
            models.WorkingConditions.id == working_conditions_id).first()
        if res:
            table_obj_dic.update({res.name_en: working_conditions_table_obj_dic["{}".format(working_conditions_id)]})
    print(table_obj_dic)
    # 表名、表对象
    for table_name, table_obj in table_obj_dic.items():
        if item.car_id_list:
            res = db.query(table_obj).filter(table_obj.coordinate_system == item.coordinate_system).filter(
                table_obj.car_base_info_id.in_(item.car_id_list)).all()
            table_obj_date_dic.update({table_name: res})
        else:
            res: [table_obj] = db.query(table_obj).filter(table_obj.coordinate_system == item.coordinate_system).all()
            table_obj_date_dic.update({table_name: res})
    return table_obj_date_dic


def get_working_conditions_detail_title(item: schemas.WorkingConditionsDetailTitle, db: Session):
    # 初始化结果字典
    working_conditions_kc_title_dic = {str(working_conditions_id): {} for working_conditions_id in
                                       item.working_conditions_list}

    # 一次性查询所有相关的 WorkingConditions 数据，减少查询次数
    working_conditions_data = db.query(models.WorkingConditions).filter(
        models.WorkingConditions.id.in_(item.working_conditions_list)
    ).all()

    # 遍历查询结果，并根据 kc_parameters_id_list 查询对应的 KCParameters
    for working_condition in working_conditions_data:
        if working_condition.kc_parameters_id_list:
            # 根据 kc_parameters_id_list 查询对应的 KCParameters
            res = db.query(models.KCParameters).filter(
                models.KCParameters.id.in_(working_condition.kc_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            working_conditions_kc_title_dic[str(working_condition.id)] = res

    return working_conditions_kc_title_dic
