from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_car_type = APIRouter(
    prefix="/car_type",
    tags=["car_type-汽车类型【轿车、SUV...】"],
)


@router_car_type.get("/", summary="获取所有汽车类型【轿车、SUV...】")
def get_car_type(db: Session = Depends(get_db)):
    return crud.get_car_type(db=db)
