from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class BrakingSystemData(BaseModel):
    coordinate_system: str
    car_id_list: Optional[List[int]] = None  # 允许 car_id 为空

    class Config:
        schema_extra = {
            "example": {
                "coordinate_system": "0",
                "car_id_list": [1, 2, 3]
            }
        }


class BrakingSystemSonDetailParameters(BaseModel):
    braking_system_son_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "braking_system_son_list": [1, 2],
            }
        }


class BrakingSystemDataOnce(BaseModel):
    car_base_info_id: int

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 1,
            }
        }


class BrakingSystemSonParametersTitle(BaseModel):
    braking_system_data_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "braking_system_data_id_list": [1, 2],  # 修改此字段名为 working_conditions_list
            }
        }


class BrakingSystemDataId(BaseModel):
    module_data_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "module_data_id_list": [1],
            }
        }


class BrakingSystemDetailAll(BaseModel):
    car_base_info_id: int
    coordinate_system: int
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 72,
                "coordinate_system": 0,
                "data": {
                    "brake_control": {'abs_module': 'ABS模块', 'epb': 'EPB',
                                      'wheel_speed_sensor': '轮速传感器', 'ipb': 'IPB',
                                      'rub': 'RUB'
                                      },
                    "brake_execution": {'front_brake_disc': '前制动盘', 'rear_brake_disc': '后制动盘',
                                        'rear_brake_drum': "后制动鼓", 'front_calipers': '前卡钳',
                                        "rear_calipers": '后卡钳',
                                        },
                }
            }
        }
