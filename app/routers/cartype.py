from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_cartype = APIRouter(
    prefix="/cartype",
    tags=["cartype-车型"],
)


@router_cartype.post("/init_data_car", summary="初始化轿车数据")
def add_init_data_car(item: schemas.CarTypeInitData, db: Session = Depends(get_db)):
    return crud.create_init_data_car(db=db, item=item)


@router_cartype.post("/init_data_suv", summary="初始化SUV数据")
def add_init_data_suv(item: schemas.CarTypeInitDataSUV, db: Session = Depends(get_db)):
    return crud.create_init_data_suv(db=db, item=item)


@router_cartype.get("/all_car", summary="获取所有的汽车")
def get_all_cartype(db: Session = Depends(get_db)):
    return crud.get_all_cartype(db=db)


@router_cartype.post("/car_or_suv", summary="获取车型数据")
def get_car_or_suv(item: schemas.CarTypeOnce, db: Session = Depends(get_db)):
    return crud.get_car_or_suv(item=item, db=db)


@router_cartype.post("/name", summary="按照name进行模糊搜索")
def search_car_by_name(item: schemas.CarTypeSearchName, db: Session = Depends(get_db)):
    return crud.search_car_by_name(item=item, db=db)


@router_cartype.post("/wheelbase", summary="按照轴距进行范围搜索")
def search_car_by_wheelbase(item: schemas.CarTypeSearchWheelBase, db: Session = Depends(get_db)):
    return crud.search_car_by_wheelbase(item=item, db=db)
