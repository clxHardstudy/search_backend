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


@router_vertical_parallel_arb_connected.post("/init_data", summary="初始化数据")
def add_init_data(item: schemas.InitData, db: Session = Depends(get_db)):
    return crud.create_init_data(db=db, item=item)
