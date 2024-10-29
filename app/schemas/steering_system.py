from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class SteeringSystemData(BaseModel):
    coordinate_system: str
    car_id_list: Optional[List[int]] = None  # 允许 car_id 为空

    class Config:
        schema_extra = {
            "example": {
                "coordinate_system": "0",
                "car_id_list": [1, 2, 3]
            }
        }


class SteeringSystemDataOnce(BaseModel):
    car_base_info_id: int

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 1,
            }
        }


class SteeringSystemSonParametersTitle(BaseModel):
    steering_system_data_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "steering_system_data_id_list": [1, 2],  # 修改此字段名为 working_conditions_list
            }
        }


class SteeringSystemDataId(BaseModel):
    module_data_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "module_data_id_list": [1],
            }
        }


class SteeringSystemDetailAll(BaseModel):
    car_base_info_id: int
    coordinate_system: int
    data: dict

    class Config:
        schema_extra = {
            "example": {
                "car_base_info_id": 72,
                "coordinate_system": 0,
                "data": {
                    "upward_turn": {'steering_column': '转向管柱',
                                    'electric_power_steering_column': '电动助力转向管柱',
                                    'electric_adjustable_steering_column': '电动可调转向管柱',
                                    'electric_adjustable_power_steering_column': '电动可调助力转向管柱',
                                    'intermediate_shaft_assembly': '中间轴总成'
                                    },
                    "downward_turn": {'mechanical_steering_gear': '机械转向器',
                                      'dp_eps': 'DP-EPS',
                                      'r_eps': "R-EPS",
                                      },
                }
            }
        }
