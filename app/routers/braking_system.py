from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

router_braking_system = APIRouter(
    prefix="/braking_system",
    tags=["braking_system-制动系统【制动控制、制动执行】"],
)


@router_braking_system.get("/", summary="获取制动系统的所有子表信息")
def get_braking_system_module(db: Session = Depends(get_db)):
    return crud.get_braking_system_module(db=db)


@router_braking_system.get("/detail_title", summary="获取制动系统的所有子表的详细字段参数")
def get_braking_system_module_parameters(db: Session = Depends(get_db)):
    return crud.get_braking_system_module_parameters(db=db)


@router_braking_system.post("/data_all", summary="获取制动系统的所属表数据【制动控制、制动执行】")
def get_braking_system_data(item: schemas.BrakingSystemData, db: Session = Depends(get_db)):
    return crud.get_braking_system_data(item=item, db=db)
