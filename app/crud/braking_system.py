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


def get_braking_system_module(db: Session):
    result: [models.BrakingSystemModule] = db.query(models.BrakingSystemModule).all()
    return result


def get_braking_system_module_parameters(db: Session):
    table_module_obj = models.BrakingSystemModule
    table_module_parameters_obj = models.BrakingSystemModuleParameters

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
        if module_once.braking_system_module_parameters_id_list:
            res = db.query(table_module_parameters_obj).filter(
                table_module_parameters_obj.id.in_(
                    module_once.braking_system_module_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            module_dic[str(module_once.id)] = res
    return module_dic


def get_braking_system_data(item: schemas.BrakingSystemData, db: Session):
    result = {}
    all_table = {
        "brake_control": models.Brake_control,
        "brake_execution": models.Brake_execution
    }
    for table_name, table_obj in all_table.items():
        filters = []
        if item.car_id_list:
            filters.append(table_obj.car_base_info_id.in_(item.car_id_list))
        if item.coordinate_system:
            filters.append(table_obj.coordinate_system == item.coordinate_system)
        result.update({table_name: db.query(table_obj).filter(*filters).all()})
    return result
