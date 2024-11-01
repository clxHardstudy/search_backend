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


def get_module_parameters_suspension(item: schemas.SuspensionSystemDataId, db: Session):
    # 初始化结果字典
    module_data_id_list = item.module_data_id_list
    module_data_son_dic = {str(module_data_id): {} for module_data_id in
                           module_data_id_list}
    table_obj = models.SuspensionSystemModule
    table_son_obj = models.SuspensionSystemModuleParameters
    # 一次性查询所有相关的 WorkingConditions 数据，减少查询次数
    module_data_list = db.query(table_obj).filter(
        table_obj.id.in_(module_data_id_list)
    ).all()
    for module_data_once in module_data_list:
        if module_data_once.suspension_system_module_parameters_id_list:
            # 根据 kc_parameters_id_list 查询对应的 KCParameters
            res = db.query(table_son_obj).filter(
                table_son_obj.id.in_(module_data_once.suspension_system_module_parameters_id_list)
            ).all()
            # 将查询结果添加到字典中
            module_data_son_dic[str(module_data_once.id)] = res
    return module_data_son_dic


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


def get_suspension_system_data_once(item: schemas.SuspensionSystemDataOnce, db: Session):
    module_system_one_list = [1, 2]
    coordinate_system = {
        "front": 0,
        "rear": 1,
    }
    # 通用模版替换处
    table_obj = models.SuspensionSystemModule
    module_system_one_table_obj_dic = {
        "1": models.Structural_Parts,
        "2": models.Elastic_Parts,
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


def update_suspension_system_detail_once(item: schemas.SuspensionSystemDetailAll, db: Session):
    token = item.token
    if not token:
        return {
            "state_code": 401,
            "reason": "没有权限"
        }
    user_id, exp = check_access_token(token, "user")
    user_obj = db.query(models.User).filter(models.User.id == user_id).first()
    if user_obj:
        if user_obj.admin_id != 1:
            return {
                "state_code": 401,
                "reason": "没有权限"
            }
    table_obj = models.SuspensionSystemModule
    car_base_info_res = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.id == item.car_base_info_id).first()
    module_son_table_list = [1, 2]
    module_system_table_obj_dic = {
        "1": models.Structural_Parts,
        "2": models.Elastic_Parts,
    }
    # 批量查询条件工况对象
    module_system = db.query(table_obj).filter(
        table_obj.id.in_(module_son_table_list)
    ).all()
    # 准备表对象字典
    table_obj_dic = {
        res.name_en: module_system_table_obj_dic[str(res.id)]
        for res in module_system
    }
    # 遍历传入的 data 字典
    for table_name, table_items in item.data.items():
        # 根据 table_name 在表对象字典中找到对应的表模型
        table_model = table_obj_dic.get(table_name)
        if not table_model:
            # 如果没找到对应的表，继续下一个
            continue
        # 查询对应的记录（根据 car_base_info_id 和 coordinate_system）
        record = db.query(table_model).filter(
            table_model.car_base_info_id == item.car_base_info_id,
            table_model.coordinate_system == item.coordinate_system
        ).first()
        if record:
            # 找到记录，更新每个字段
            for field, value in table_items.items():
                if hasattr(record, field):
                    setattr(record, field, value)  # 动态更新字段
            print("找到目标，更新！")
        else:
            print("未找到目标：跳过！")
            # 如果没有找到记录，可以选择创建新的记录（如果这是你想要的行为）
            # new_record = table_model(
            #     car_base_info_id=item.car_base_info_id,
            #     coordinate_system=item.coordinate_system,
            #     car_type_id=car_base_info_res.car_type_id,
            #     **table_items
            # )
            # db.add(new_record)
    # 提交所有修改
    db.commit()
    db.flush()
