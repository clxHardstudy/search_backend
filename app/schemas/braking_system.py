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
