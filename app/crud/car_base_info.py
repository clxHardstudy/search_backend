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


def create_init_data_car(db: Session, item: schemas.CarBaseInfoListInitData):
    carinitdata_list = item.carinitdata
    rowdata = {}
    for car_data_dic in carinitdata_list:
        res: models.CarBaseInfo = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.name == car_data_dic.name).first()
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
                "car_type_id": car_data_dic.car_type_id
            }
        )
        db_item = models.CarBaseInfo(**rowdata)
        db.add(db_item)
        db.commit()
        db.flush()
        # print(rowdata)


def create_init_data_suv(db: Session, item: schemas.CarBaseInfoListInitDataSUV):
    carinitdata_list = item.carinitdata
    rowdata = {}
    for car_data_dic in carinitdata_list:
        res: models.CarBaseInfo = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.name == car_data_dic.name).first()
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
                "car_type_id": car_data_dic.car_type_id
            }
        )
        db_item = models.CarBaseInfo(**rowdata)
        db.add(db_item)
        db.commit()
        db.flush()
        # print(rowdata)


def get_all_car_base_info(db: Session):
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).all()
    return result


def get_car_or_suv(item: schemas.CarBaseInfoOnce, db: Session):
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.car_type_id == item.id).all()
    # print(result)
    return result


def search_car_by_name(item: schemas.CarBaseInfoSearchName, db: Session):
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.name.ilike(f"%{item.name}%")).all()
    # print(result)
    return result


def search_car_by_wheelbase(item: schemas.CarBaseInfoSearchWheelBase, db: Session):
    # 拆分 wheelbase，确保有有效的左值和右值
    wheelbase = item.wheelbase.split("-")
    # 初始化左值和右值为 None
    left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    if left and right:
        result = db.query(models.CarBaseInfo).filter(
            models.CarBaseInfo.wheelbase.between(left, right)
        ).all()
    elif left:
        result = db.query(models.CarBaseInfo).filter(
            models.CarBaseInfo.wheelbase == left
        ).all()
    elif right:
        result = db.query(models.CarBaseInfo).filter(
            models.CarBaseInfo.wheelbase == right
        ).all()
    else:
        result = []  # 如果没有输入任何有效的数值，则返回空列表
    return result


def search_car_by_name_and_wheelbase(item: schemas.CarBaseInfoSearchNameAndWheelBase, db: Session):
    # 首先根据 name 进行模糊查询
    query = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.name.ilike(f"%{item.name}%"))
    # 拆分 wheelbase，确保有有效的左值和右值
    wheelbase = item.wheelbase.split("-")
    # 初始化左值和右值为 None
    left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    # 根据轴距范围进行进一步过滤
    if left and right:
        query = query.filter(models.CarBaseInfo.wheelbase.between(left, right))
    elif left:
        query = query.filter(models.CarBaseInfo.wheelbase == left)
    elif right:
        query = query.filter(models.CarBaseInfo.wheelbase == right)
    # 执行查询并获取结果
    result = query.all()
    return result

