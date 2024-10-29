from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

router_suspension_system = APIRouter(
    prefix="/suspension_system",
    tags=["suspension_system-悬架系统【前悬架、后悬架】"],
)


@router_suspension_system.get("/", summary="获取悬架系统的所有子表信息")
def get_suspension_system_module(db: Session = Depends(get_db)):
    return crud.get_suspension_system_module(db=db)


@router_suspension_system.get("/detail_title", summary="获取悬架系统的所有子表的详细字段参数")
def get_suspension_system_module_parameters(db: Session = Depends(get_db)):
    return crud.get_suspension_system_module_parameters(db=db)


@router_suspension_system.post("/son_detail_title", summary="获取悬架系统的所有子表的详细字段参数")
def get_suspension_system_module_parameters(item: schemas.SuspensionSystemDataId, db: Session = Depends(get_db)):
    return crud.get_module_parameters_suspension(item=item, db=db)


@router_suspension_system.post("/data_all", summary="获取悬架系统的所属表数据【结构件、弹性件】")
def get_suspension_system_data(item: schemas.SuspensionSystemData, db: Session = Depends(get_db)):
    return crud.get_suspension_system_data(item=item, db=db)


@router_suspension_system.post("/detail_once", summary="获取某个模版的所有子表参数数值")
def get_suspension_system_detail_once(item: schemas.SuspensionSystemDataOnce, db: Session = Depends(get_db)):
    return crud.get_suspension_system_data_once(item=item, db=db)


@router_suspension_system.post("/update_detail_once", summary="修改某个汽车的悬架系统")
def update_suspension_system_detail_once(item: schemas.SuspensionSystemDetailAll, db: Session = Depends(get_db)):
    return crud.update_suspension_system_detail_once(item=item, db=db)
