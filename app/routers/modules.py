from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_modules = APIRouter(
    prefix="/modules",
    tags=["modules-模块【K&C｜前悬架｜后悬架...】"],
)


@router_modules.get("/", summary="获取所有模块类型【K&C｜前悬架｜后悬架...】")
def get_modules(db: Session = Depends(get_db)):
    return crud.get_modules(db=db)
