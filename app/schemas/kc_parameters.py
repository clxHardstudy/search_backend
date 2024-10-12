from typing import Optional, List
from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


# 定义 WorkingConditions 模型
class KCParameters(BaseModel):
    kc_parameters_id_list: Optional[List[int]] = None

    class Config:
        schema_extra = {
            "example": {
                "kc_parameters_id_list": [1, 2, 3],  # 修改此字段名为 working_conditions_list
            }
        }
