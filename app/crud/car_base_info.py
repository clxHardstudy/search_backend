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


def get_car_base_info_list(item: schemas.CarBaseInfoList, db: Session):
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(
        models.CarBaseInfo.id.in_(item.car_base_info_id_list)).all()
    return result


def get_car_or_suv(item: schemas.CarBaseInfoOnce, db: Session):
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.car_type_id == item.id).all()
    return result


def get_car_by_car_type_and_platform(item: schemas.CarBaseInfoCarTypeAndPlatform, db: Session):
    # print(item.car_type_id, item.platform_id_list)
    filters = []
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    if item.platform_id_list:
        filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
    result: [models.CarBaseInfo] = db.query(models.CarBaseInfo).filter(*filters).all()
    return result


def search_car_by_name(item: schemas.CarBaseInfoSearchName, db: Session):
    # 构建查询条件列表
    filters = []
    # 车型类型筛选
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    if item.platform_id_list:
        filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
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
    # print(wheelbase)
    # 初始化左值和右值，确保转换为数值类型
    left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    # 构建查询条件列表
    filters = []
    # 车型类型筛选
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    if item.platform_id_list:
        filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
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
    # print(item.car_type_id, item.platform_id_list, item.name, item.wheelbase)
    filters = []
    # 如果存在 car_type_id，则添加过滤条件
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    if item.platform_id_list:
        filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
    if item.name:
        filters.append(models.CarBaseInfo.name.ilike(f"%{item.name}%"))
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


def search_car_by_multiple_condition_query(item: schemas.CarBaseInfoMultipleConditionQuery, db: Session):
    filters = []
    # 如果存在 car_type_id，则添加过滤条件
    if item.car_type_id:
        filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
    if item.platform_id_list:
        filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
    if item.name:
        filters.append(models.CarBaseInfo.name.ilike(f"%{item.name}%"))
    # 拆分 wheelbase，确保有有效的左值和右值
    wheelbase = item.wheelbase.split("-")
    front_track = item.front_track.split("-")
    rear_track = item.rear_track.split("-")
    # 初始化左值和右值
    wheelbase_left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
    wheelbase_right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
    front_track_left = front_track[0] if len(front_track) > 0 and front_track[0] else None
    front_track_right = front_track[1] if len(front_track) > 1 and front_track[1] else None
    rear_track_left = rear_track[0] if len(rear_track) > 0 and rear_track[0] else None
    rear_track_right = rear_track[1] if len(rear_track) > 1 and rear_track[1] else None
    # 根据轴距范围添加过滤条件
    if wheelbase_left and wheelbase_right:
        filters.append(models.CarBaseInfo.wheelbase.between(wheelbase_left, wheelbase_right))
    elif wheelbase_left:
        filters.append(models.CarBaseInfo.wheelbase == wheelbase_left)
    elif wheelbase_right:
        filters.append(models.CarBaseInfo.wheelbase == wheelbase_right)

    if front_track_left and front_track_right:
        filters.append(models.CarBaseInfo.front_track.between(front_track_left, front_track_right))
    elif front_track_left:
        filters.append(models.CarBaseInfo.front_track == front_track_left)
    elif front_track_right:
        filters.append(models.CarBaseInfo.front_track == front_track_right)

    if rear_track_left and rear_track_right:
        filters.append(models.CarBaseInfo.rear_track.between(rear_track_left, rear_track_right))
    elif rear_track_left:
        filters.append(models.CarBaseInfo.rear_track == rear_track_left)
    elif rear_track_right:
        filters.append(models.CarBaseInfo.rear_track == rear_track_right)
    # 执行查询并返回结果
    result = db.query(models.CarBaseInfo).filter(*filters).all()
    return result


def search_car_by_new_multiple_condition_query(item: schemas.CarBaseInfoNewMultipleConditionQuery, db: Session):
    filters = []
    # 如果存在 car_type_id，则添加过滤条件
    if item.car_base_info_id_list:
        result = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.id.in_(item.car_base_info_id_list)).all()
    else:
        if item.car_type_id:
            filters.append(models.CarBaseInfo.car_type_id == item.car_type_id)
        if item.platform_id_list:
            filters.append(models.CarBaseInfo.platform_id.in_(item.platform_id_list))
        if item.name:
            filters.append(models.CarBaseInfo.name.ilike(f"%{item.name}%"))
        # 拆分 wheelbase，确保有有效的左值和右值
        wheelbase = item.wheelbase.split("-")
        front_track = item.front_track.split("-")
        rear_track = item.rear_track.split("-")
        # 初始化左值和右值
        wheelbase_left = wheelbase[0] if len(wheelbase) > 0 and wheelbase[0] else None
        wheelbase_right = wheelbase[1] if len(wheelbase) > 1 and wheelbase[1] else None
        front_track_left = front_track[0] if len(front_track) > 0 and front_track[0] else None
        front_track_right = front_track[1] if len(front_track) > 1 and front_track[1] else None
        rear_track_left = rear_track[0] if len(rear_track) > 0 and rear_track[0] else None
        rear_track_right = rear_track[1] if len(rear_track) > 1 and rear_track[1] else None
        # 根据轴距范围添加过滤条件
        if wheelbase_left and wheelbase_right:
            filters.append(models.CarBaseInfo.wheelbase.between(wheelbase_left, wheelbase_right))
        elif wheelbase_left:
            filters.append(models.CarBaseInfo.wheelbase == wheelbase_left)
        elif wheelbase_right:
            filters.append(models.CarBaseInfo.wheelbase == wheelbase_right)

        if front_track_left and front_track_right:
            filters.append(models.CarBaseInfo.front_track.between(front_track_left, front_track_right))
        elif front_track_left:
            filters.append(models.CarBaseInfo.front_track == front_track_left)
        elif front_track_right:
            filters.append(models.CarBaseInfo.front_track == front_track_right)

        if rear_track_left and rear_track_right:
            filters.append(models.CarBaseInfo.rear_track.between(rear_track_left, rear_track_right))
        elif rear_track_left:
            filters.append(models.CarBaseInfo.rear_track == rear_track_left)
        elif rear_track_right:
            filters.append(models.CarBaseInfo.rear_track == rear_track_right)
        # 执行查询并返回结果
        result = db.query(models.CarBaseInfo).filter(*filters).all()
    return result
