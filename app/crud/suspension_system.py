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


def get_suspension_system_module(db: Session):
    result: [models.SuspensionSystemModule] = db.query(models.SuspensionSystemModule).all()
    return result


def get_suspension_system_module_parameters(db: Session):
    query = db.query(models.SuspensionSystemModule).all()
    suspension_system_module_id_list = []
    for once in query:
        suspension_system_module_id_list.append(once.id)
    # 初始化结果字典
    suspension_system_module_dic = {str(suspension_system_module_id): {} for suspension_system_module_id in
                                    suspension_system_module_id_list}
    # 一次性查询所有相关的 WorkingConditions 数据，减少查询次数
    suspension_system_module_data = db.query(models.SuspensionSystemModule).filter(
        models.SuspensionSystemModule.id.in_(suspension_system_module_id_list)
    ).all()
    for suspension_system_module_once in suspension_system_module_data:
        if suspension_system_module_once.suspension_system_module_parameters_id_list:
            res = db.query(models.SuspensionSystemModuleParameters).filter(
                models.SuspensionSystemModuleParameters.id.in_(
                    suspension_system_module_once.suspension_system_module_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            suspension_system_module_dic[str(suspension_system_module_once.id)] = res
    return suspension_system_module_dic


def get_suspension_system_data(item: schemas.SuspensionSystemData, db: Session):
    result = {}
    all_table = {
        "structural_parts": models.Structural_Parts,
        "elastic_parts": models.Elastic_Parts
    }
    res = db.query(models.Structural_Parts).filter(models.Structural_Parts.car_base_info_id.in_(item.car_id_list))
    for table_name, table_obj in all_table.items():
        filters = []
        if item.car_id_list:
            filters.append(table_obj.car_base_info_id.in_(item.car_id_list))
        if item.coordinate_system:
            filters.append(table_obj.coordinate_system == item.coordinate_system)
        result.update({table_name: db.query(table_obj).filter(*filters).all()})
    return result
