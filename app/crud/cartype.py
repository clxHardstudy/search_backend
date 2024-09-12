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


def create_init_data_car(db: Session, item: schemas.CarTypeInitData):
    carinitdata_list = item.carinitdata
    rowdata = {}
    for car_data_dic in carinitdata_list:
        res: models.CarType = db.query(models.CarType).filter(models.CarType.name == car_data_dic.name).first()
        if res:
            print(car_data_dic.name + "-车型已存在，无法插入该条数据")
            continue
        now = int(time.time())
        rowdata.update(
            {
                "name": car_data_dic.name,
                "wheelbase": car_data_dic.wheelbase,
                "release_date": car_data_dic.release_date,
                "create_time": now,
                "update_time": now,
                "category": car_data_dic.category
            }
        )
        db_item = models.CarType(**rowdata)
        db.add(db_item)
        db.commit()
        db.flush()
        # print(rowdata)


def create_init_data_suv(db: Session, item: schemas.CarTypeInitDataSUV):
    carinitdata_list = item.carinitdata
    rowdata = {}
    for car_data_dic in carinitdata_list:
        res: models.CarType = db.query(models.CarType).filter(models.CarType.name == car_data_dic.name).first()
        if res:
            print(car_data_dic.name + "-车型已存在，无法插入该条数据")
            continue
        now = int(time.time())
        rowdata.update(
            {
                "name": car_data_dic.name,
                "wheelbase": car_data_dic.wheelbase,
                "release_date": car_data_dic.release_date,
                "create_time": now,
                "update_time": now,
                "category": car_data_dic.category
            }
        )
        db_item = models.CarType(**rowdata)
        db.add(db_item)
        db.commit()
        db.flush()
        # print(rowdata)


def get_all_cartype(db: Session):
    result: [models.CarType] = db.query(models.CarType).all()
    return result


def get_car_or_suv(item: schemas.CarTypeOnce, db: Session):
    result: [models.CarType] = db.query(models.CarType).filter(models.CarType.category == item.id).all()
    # print(result)
    return result


def search_car_by_name(item: schemas.CarTypeSearchName, db: Session):
    result: [models.CarType] = db.query(models.CarType).filter(models.CarType.name.ilike(f"%{item.name}%")).all()
    # print(result)
    return result


def search_car_by_wheelbase(item: schemas.CarTypeSearchWheelBase, db: Session):
    if item.WheelBase_Large and item.WheelBase_Small:
        result: [models.CarType] = db.query(models.CarType).filter(
            models.CarType.wheelbase.between(item.WheelBase_Small, item.WheelBase_Large)).all()
    elif item.WheelBase_Small:
        result: [models.CarType] = db.query(models.CarType).filter(
            models.CarType.wheelbase == item.WheelBase_Small).all()
    elif item.WheelBase_Large:
        result: [models.CarType] = db.query(models.CarType).filter(
            models.CarType.wheelbase == item.WheelBase_Large).all()
    else:
        return []
    # print(result)
    return result
