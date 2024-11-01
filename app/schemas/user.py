from typing import Union, Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class UserCreate(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "user",
                "password": "user"}}


class UserUpdate(BaseModel):
    password: Optional[str] = None


class UserGet(BaseModel):
    create_time: Union[int, None] = None
    last_login: Union[int, None] = None


class UserSwaggerLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "name": "clx",
                "password": "020905",
            }}


class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        schema_extra = {
            "example": {
                "username": "clx",
                "password": "020905",
            }}


class UserToken(BaseModel):
    token: str

    class Config:
        schema_extra = {
            "example": {
                "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJOb25lIiwiZXhwIjoxNzMwNTM2MzI4fQ.MRp9i775T6SGXCQMSHDVRdo9zMZzZUuYuIiqa8JUmTs",
            }}


class User(BaseModel):
    id: int
    name: str
    password: str
    auth_token: str
    create_time: int
    update_time: int
    last_login: int

    class Config:
        orm_mode = True
