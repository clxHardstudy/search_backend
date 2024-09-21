from typing import Union, Optional
from typing import Union, Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


# 定义 WorkingConditions 模型
class WorkingConditions(BaseModel):
    coordinate_system: str
    working_conditions_list: List[int]  # 确保类型是 List[int]
    car_id_list: Optional[List[int]] = None  # 允许 car_id 为空

    class Config:
        schema_extra = {
            "example": {
                "coordinate_system": "0",
                "working_conditions_list": [1, 2, 3],  # 修改此字段名为 working_conditions_list
                "car_id_list": [1, 2, 3]
            }
        }


class WorkingConditionsDetailTitle(BaseModel):
    working_conditions_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "working_conditions_list": [1, 2, 3],  # 修改此字段名为 working_conditions_list
            }
        }
