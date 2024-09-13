from typing import Union, Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


# class CarType(BaseModel):
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "": "",
#                 "": ""}}
