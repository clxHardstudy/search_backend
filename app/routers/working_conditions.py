from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_working_conditions = APIRouter(
    prefix="/working_conditions",
    tags=["working_conditions-工况汇总"],
)


@router_working_conditions.get("/", summary="获取所有工况")
def get_working_conditions(db: Session = Depends(get_db)):
    return crud.get_working_conditions(db=db)


@router_working_conditions.post("/detail", summary="获取工况性能参数数值")
def get_working_conditions_detail(item: schemas.WorkingConditions, db: Session = Depends(get_db)):
    return crud.get_working_conditions_detail(item=item, db=db)


@router_working_conditions.post("/detail_once", summary="获取某个汽车的所有工况参数数值")
def get_working_conditions_detail_once(item: schemas.WorkingConditionsDetailOnce, db: Session = Depends(get_db)):
    return crud.get_working_conditions_detail_once(item=item, db=db)


@router_working_conditions.post("/update_detail_once", summary="修改某个汽车的所有工况参数数值")
def update_working_conditions_detail_once(item: schemas.WorkingConditionsDetailAll, db: Session = Depends(get_db)):
    return crud.update_working_conditions_detail_once(item=item, db=db)


@router_working_conditions.post("/detail_title", summary="获取工况性能参数名称")
def get_working_conditions_detail_title(item: schemas.WorkingConditionsDetailTitle, db: Session = Depends(get_db)):
    return crud.get_working_conditions_detail_title(item=item, db=db)
