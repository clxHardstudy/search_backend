import time

from app import models, schemas
from sqlalchemy.orm import Session
from decimal import Decimal, ROUND_DOWN


def get_working_conditions(db: Session):
    """
    获取全部工况
    :param db:
    :return:
    """
    result: [models.WorkingConditions] = db.query(models.WorkingConditions).all()
    return result


def get_working_conditions_detail(item: schemas.WorkingConditions, db: Session):
    """
    获取待查询工况全部信息
    :param item:
    :param db:
    :return:
    """
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
    # 批量查询条件工况对象
    working_conditions = db.query(models.WorkingConditions).filter(
        models.WorkingConditions.id.in_(item.working_conditions_list)
    ).all()

    # 准备表对象字典
    table_obj_dic = {
        res.name_en: working_conditions_table_obj_dic[str(res.id)]
        for res in working_conditions
    }
    table_obj_date_dic = {}
    # 查询表并保留小数位
    for table_name, table_obj in table_obj_dic.items():
        # 构建查询条件
        query = db.query(table_obj).filter(table_obj.coordinate_system == item.coordinate_system)
        if item.car_id_list:
            query = query.filter(table_obj.car_base_info_id.in_(item.car_id_list))
        # 一次性获取数据
        res_list = query.all()
        # 对查询结果进行小数位处理
        formatted_res_list = []
        for res in res_list:
            for attr, value in vars(res).items():
                # 仅处理浮点数或字符串的数字
                if isinstance(value, float):
                    setattr(res, attr, round(value, 3))
                elif isinstance(value, str) and is_float_or_int(value):
                    decimal_value = format_decimal(value)
                    if float(decimal_value) != float(value):
                        setattr(res, attr, decimal_value)
            formatted_res_list.append(res)
        table_obj_date_dic.update({table_name: formatted_res_list})
    return table_obj_date_dic


def get_working_conditions_detail_once(item: schemas.WorkingConditionsDetailOnce, db: Session):
    """
    获取某一个汽车待查询工况全部信息
    :param item:
    :param db:
    :return:
    """
    working_conditions_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    coordinate_system = {
        "front": 0,
        "rear": 1,
    }
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
    # 批量查询条件工况对象
    working_conditions = db.query(models.WorkingConditions).filter(
        models.WorkingConditions.id.in_(working_conditions_list)
    ).all()
    # 准备表对象字典
    table_obj_dic = {
        res.name_en: working_conditions_table_obj_dic[str(res.id)]
        for res in working_conditions
    }

    table_obj_date_dic = {"front": {}, "rear": {}}
    for table_name, table_obj in table_obj_dic.items():
        for coordinate_system_key, coordinate_system_value in coordinate_system.items():
            res = db.query(table_obj).filter(table_obj.car_base_info_id == item.car_base_info_id).filter(
                table_obj.coordinate_system == coordinate_system_value).all()
            table_obj_date_dic[coordinate_system_key].update({table_name: res})
    # print(table_obj_date_dic)
    return table_obj_date_dic


def update_working_conditions_detail_once(item: schemas.WorkingConditionsDetailAll, db: Session):
    """
    修改某一个汽车工况的所有信息
    :param item: 传入的WorkingConditionsDetailAll对象
    :param db: 数据库会话
    :return: None
    """
    car_base_info_res = db.query(models.CarBaseInfo).filter(models.CarBaseInfo.id == item.car_base_info_id).first()
    working_conditions_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
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
    # 批量查询条件工况对象
    working_conditions = db.query(models.WorkingConditions).filter(
        models.WorkingConditions.id.in_(working_conditions_list)
    ).all()
    # 准备表对象字典
    table_obj_dic = {
        res.name_en: working_conditions_table_obj_dic[str(res.id)]
        for res in working_conditions
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
        else:
            # 如果没有找到记录，可以选择创建新的记录（如果这是你想要的行为）
            new_record = table_model(
                car_base_info_id=item.car_base_info_id,
                coordinate_system=item.coordinate_system,
                car_type_id=car_base_info_res.car_type_id,
                **table_items
            )
            db.add(new_record)
    # 提交所有修改
    db.commit()
    db.flush()


def get_working_conditions_detail_title(item: schemas.WorkingConditionsDetailTitle, db: Session):
    """
    获取工况对应的KC参数
    :param item:
    :param db:
    :return:
    """
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


def is_float_or_int(value):
    """
    判断是否为可转换为浮点数或整数的字符串
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def format_decimal(value):
    """
    只保留超过三位小数的数字到三位小数，否则保持原样
    """
    decimal_value = Decimal(value)
    if decimal_value.as_tuple().exponent < -3:
        # 如果小数位超过三位，保留三位小数
        return decimal_value.quantize(Decimal('0.000'), rounding=ROUND_DOWN)
    else:
        # 小数位少于或等于三位，不改变
        return decimal_value
