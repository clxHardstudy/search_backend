from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

router_traditional_four_wheel_drive_system = APIRouter(
    prefix="/traditional_four_wheel_drive_system",
    tags=["traditional_four_wheel_drive_system-传动四驱系统【传动、悬置】"],
)


@router_traditional_four_wheel_drive_system.get("/", summary="获取制动系统的所有子表信息")
def get_traditional_four_wheel_drive_system_module(db: Session = Depends(get_db)):
    return crud.get_traditional_four_wheel_drive_system_module(db=db)


@router_traditional_four_wheel_drive_system.get("/detail_title", summary="获取制动系统的所有子表的详细字段参数")
def get_traditional_four_wheel_drive_system_module_parameters(db: Session = Depends(get_db)):
    return crud.get_traditional_four_wheel_drive_system_module_parameters(db=db)


@router_traditional_four_wheel_drive_system.post("/data_all", summary="获取制动系统的所属表数据【制动控制、制动执行】")
def get_traditional_four_wheel_drive_system_data(item: schemas.TraditionalFourWheelDriveSystemData, db: Session = Depends(get_db)):
    return crud.get_traditional_four_wheel_drive_system_data(item=item, db=db)
