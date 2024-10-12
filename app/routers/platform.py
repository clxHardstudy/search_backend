from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

router_platform = APIRouter(
    prefix="/platform",
    tags=["platform-平台类型【T1X、T2X...】"],
)


@router_platform.get("/", summary="获取所有平台类型【T1X、T2X...】")
def get_car_type(db: Session = Depends(get_db)):
    return crud.get_platform(db=db)
