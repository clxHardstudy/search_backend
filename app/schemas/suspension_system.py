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
