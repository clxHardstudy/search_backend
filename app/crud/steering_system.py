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


def get_steering_system_module(db: Session):
    result: [models.SteeringSystemModule] = db.query(models.SteeringSystemModule).all()
    return result


def get_steering_system_module_parameters(db: Session):
    table_module_obj = models.SteeringSystemModule
    table_module_parameters_obj = models.SteeringSystemModuleParameters

    query = db.query(table_module_obj).all()
    module_id_list = []
    for once in query:
        module_id_list.append(once.id)
    # 初始化结果字典
    module_dic = {str(module_id): {} for module_id in
                  module_id_list}
    module_data = db.query(table_module_obj).filter(
        table_module_obj.id.in_(module_id_list)
    ).all()
    for module_once in module_data:
        # 通用这里的参数需要修改
        if module_once.steering_system_module_parameters_id_list:
            res = db.query(table_module_parameters_obj).filter(
                table_module_parameters_obj.id.in_(
                    module_once.steering_system_module_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            module_dic[str(module_once.id)] = res
    return module_dic


def get_module_parameters_steering(item: schemas.SteeringSystemDataId, db: Session):
    # 初始化结果字典
    module_data_id_list = item.module_data_id_list
    module_data_son_dic = {str(module_data_id): {} for module_data_id in
                           module_data_id_list}
    table_obj = models.SteeringSystemModule
    table_son_obj = models.SteeringSystemModuleParameters
    module_data_list = db.query(table_obj).filter(
        table_obj.id.in_(module_data_id_list)
    ).all()
    for module_data_once in module_data_list:
        if module_data_once.steering_system_module_parameters_id_list:
            # 根据 kc_parameters_id_list 查询对应的 KCParameters
            res = db.query(table_son_obj).filter(
                table_son_obj.id.in_(module_data_once.steering_system_module_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            module_data_son_dic[str(module_data_once.id)] = res
    return module_data_son_dic


def get_steering_system_data(item: schemas.SteeringSystemData, db: Session):
    result = {}
    all_table = {
        "upward_turn": models.Upward_turn,
        "downward_turn": models.Downward_turn
    }
    for table_name, table_obj in all_table.items():
        filters = []
        if item.car_id_list:
            filters.append(table_obj.car_base_info_id.in_(item.car_id_list))
        if item.coordinate_system:
            filters.append(table_obj.coordinate_system == item.coordinate_system)
        result.update({table_name: db.query(table_obj).filter(*filters).all()})
    return result


def get_steering_system_data_once(item: schemas.SteeringSystemDataOnce, db: Session):
    module_system_one_list = [1, 2]
    coordinate_system = {
        "front": 0,
        "rear": 1,
    }
    # 通用模版替换处
    table_obj = models.SteeringSystemModule
    module_system_one_table_obj_dic = {
        "1": models.Upward_turn,
        "2": models.Downward_turn,
    }
    # 批量查询条件工况对象
    module_system_data = db.query(table_obj).filter(table_obj.id.in_(module_system_one_list)).all()
    # 准备表对象字典
    table_obj_dic = {
        res.name_en: module_system_one_table_obj_dic[str(res.id)]
        for res in module_system_data
    }

    table_obj_date_dic = {"front": {}, "rear": {}}
    for table_name, table_obj in table_obj_dic.items():
        for coordinate_system_key, coordinate_system_value in coordinate_system.items():
            res = db.query(table_obj).filter(table_obj.car_base_info_id == item.car_base_info_id).filter(
                table_obj.coordinate_system == coordinate_system_value).all()
            table_obj_date_dic[coordinate_system_key].update({table_name: res})
    return table_obj_date_dic
