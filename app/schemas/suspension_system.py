from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class SuspensionSystemData(BaseModel):
    coordinate_system: str
    car_id_list: Optional[List[int]] = None  # 允许 car_id 为空

    class Config:
        schema_extra = {
            "example": {
                "coordinate_system": "0",
                "car_id_list": [1, 2, 3]
            }
        }


class SuspensionSystemSonDetailParameters(BaseModel):
    suspension_system_son_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "suspension_system_son_list": [1, 2],
            }
        }


class SuspensionSystemDataOnce(BaseModel):
    car_base_info_id: int

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 1,
            }
        }


class SuspensionSystemDataId(BaseModel):
    module_data_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "module_data_id_list": [1],
            }
        }


class SuspensionSystemDetailAll(BaseModel):
    car_base_info_id: int
    coordinate_system: int
    data: dict
    token: str

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 72,
                "coordinate_system": 0,
                "data": {
                    "structural_parts": {'subframe': '副车架', 'front_upper_control_arm': '前上控制臂',
                                         'rear_upper_control_arm': '后上控制臂', 'front_down_control_arm': '前下控制臂',
                                         'rear_down_control_arm': '后下控制臂', 'front_arm': '前束臂',
                                         },
                    "elastic_parts": {'shock_absorbers': '减震器', 'spring': '弹簧',
                                      'stabilizer_bar': "稳定杆", 'connecting_rod': '连接杆',
                                      "bushing": '衬套', 'ball_pin': '球销',
                                      },
                }
            }
        }
