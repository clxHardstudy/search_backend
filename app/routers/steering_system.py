from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

router_steering_system = APIRouter(
    prefix="/steering_system",
    tags=["steering_system-转向系统【上转向、下转向】"],
)


@router_steering_system.get("/", summary="获取转向系统的所有子表信息")
def get_steering_system_module(db: Session = Depends(get_db)):
    return crud.get_steering_system_module(db=db)


@router_steering_system.get("/detail_title", summary="获取转向系统的所有子表的详细字段参数")
def get_steering_system_module_parameters(db: Session = Depends(get_db)):
    return crud.get_steering_system_module_parameters(db=db)


@router_steering_system.post("/data_all", summary="获取转向系统的所属表数据【上转向、下转向】")
def get_steering_system_data(item: schemas.SteeringSystemData, db: Session = Depends(get_db)):
    return crud.get_steering_system_data(item=item, db=db)
