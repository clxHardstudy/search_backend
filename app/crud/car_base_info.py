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
        res: models.CarBaseInfo = db.query(models.CarBaseInfo).filter(
            models.CarBaseInfo.name == car_data_dic.name).first()
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
        res: models.CarBaseInfo = db.query(models.CarBaseInfo).filter(
            models.CarBaseInfo.name == car_data_dic.name).first()
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
    return result


def search_car_by_name(item: schemas.CarBaseInfoSearchName, db: Session):
    # 构建查询条件列表
    filters = []
    # 车型类型筛选
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    # 名称模糊搜索
    if item.name:
        filters.append(models.CarBaseInfo.name.ilike(f"%{item.name}%"))
    # 执行查询，如果没有任何条件则返回空列表
    if filters:
        result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(*filters).all()
    else:
        result = []
    return result


def search_car_by_wheelbase(item: schemas.CarBaseInfoSearchWheelBase, db: Session):
    # 拆分 wheelbase，确保有有效的左值和右值
    wheelbase = item.wheelbase.split("-")
    # 初始化左值和右值，确保转换为数值类型
    left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    # 构建查询条件列表
    filters = []
    # 车型类型筛选
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    # 轴距范围筛选
    if left and right:
        filters.append(models.CarBaseInfo.wheelbase.between(left, right))
    elif left:
        filters.append(models.CarBaseInfo.wheelbase == left)
    elif right:
        filters.append(models.CarBaseInfo.wheelbase == right)
    # 执行查询，如果没有任何条件则返回空列表
    if filters:
        result = db.query(models.CarBaseInfo).filter(*filters).all()
    else:
        result = []
    return result


def search_car_by_name_and_wheelbase(item: schemas.CarBaseInfoSearchNameAndWheelBase, db: Session):
    # 初始化查询条件列表
    filters = [models.CarBaseInfo.name.ilike(f"%{item.name}%")]
    # 如果存在 car_type_id，则添加过滤条件
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    # 拆分 wheelbase，确保有有效的左值和右值
    wheelbase = item.wheelbase.split("-")
    # 初始化左值和右值
    left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    # 根据轴距范围添加过滤条件
    if left and right:
        filters.append(models.CarBaseInfo.wheelbase.between(left, right))
    elif left:
        filters.append(models.CarBaseInfo.wheelbase == left)
    elif right:
        filters.append(models.CarBaseInfo.wheelbase == right)
    # 执行查询并返回结果
    result = db.query(models.CarBaseInfo).filter(*filters).all()
    return result
