from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_vertical_parallel_arb_connected = APIRouter(
    prefix="/vertical_parallel_arb_connected",
    tags=["vertical_parallel_arb_connected-垂直平行工况(稳定杆连接)"],
)


@router_vertical_parallel_arb_connected.get("/", summary="获取【垂直平行工况(稳定杆连接)】KC参数")
def get_vertical_parallel_arb_connected(db: Session = Depends(get_db)):
    return crud.get_vertical_parallel_arb_connected(db=db)


@router_vertical_parallel_arb_connected.get("/car_type/{item_id}",
                                            summary="依据汽车类型去获取【垂直平行工况(稳定杆连接)】KC参数")
def get_vertical_parallel_arb_connected(item_id: int, db: Session = Depends(get_db)):
    return crud.get_vertical_parallel_arb_connected_by_car_type_id(item_id=item_id, db=db)
