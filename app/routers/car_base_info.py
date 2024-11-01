from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models

from configs.setting import config

router_car_base_info = APIRouter(
    prefix="/car_base_info",
    tags=["car_base_info-汽车基本信息"],
)


@router_car_base_info.post("/init_data_car", summary="初始化轿车数据")
def add_init_data_car(item: schemas.CarBaseInfoListInitData, db: Session = Depends(get_db)):
    return crud.create_init_data_car(db=db, item=item)


@router_car_base_info.post("/init_data_suv", summary="初始化SUV数据")
def add_init_data_suv(item: schemas.CarBaseInfoListInitDataSUV, db: Session = Depends(get_db)):
    return crud.create_init_data_suv(db=db, item=item)


@router_car_base_info.get("/all_car", summary="获取所有的汽车")
def get_all_car_base_info(db: Session = Depends(get_db)):
    return crud.get_all_car_base_info(db=db)


@router_car_base_info.post("/car_list", summary="获取列表中的这些汽车")
def get_car_base_info_list(item: schemas.CarBaseInfoList, db: Session = Depends(get_db)):
    return crud.get_car_base_info_list(item=item, db=db)


@router_car_base_info.post("/car_or_suv", summary="获取不同车型数据")
def get_car_or_suv(item: schemas.CarBaseInfoOnce, db: Session = Depends(get_db)):
    return crud.get_car_or_suv(item=item, db=db)


@router_car_base_info.post("/car_type_and_platform", summary="获取不同平台的车型数据")
def get_car_or_suv(item: schemas.CarBaseInfoCarTypeAndPlatform, db: Session = Depends(get_db)):
    return crud.get_car_by_car_type_and_platform(item=item, db=db)


@router_car_base_info.post("/name", summary="按照name进行模糊搜索")
def search_car_by_name(item: schemas.CarBaseInfoSearchName, db: Session = Depends(get_db)):
    return crud.search_car_by_name(item=item, db=db)


@router_car_base_info.post("/wheelbase", summary="按照轴距进行范围搜索")
def search_car_by_wheelbase(item: schemas.CarBaseInfoSearchWheelBase, db: Session = Depends(get_db)):
    return crud.search_car_by_wheelbase(item=item, db=db)


@router_car_base_info.post("/name_and_wheelbase", summary="按照名称和轴距进行范围搜索")
def search_car_by_name_wheelbase(item: schemas.CarBaseInfoSearchNameAndWheelBase, db: Session = Depends(get_db)):
    return crud.search_car_by_name_and_wheelbase(item=item, db=db)


@router_car_base_info.post("/multiple_condition_query", summary="多条件查询")
def search_car_by_multiple_condition_query(item: schemas.CarBaseInfoMultipleConditionQuery,
                                           db: Session = Depends(get_db)):
    return crud.search_car_by_multiple_condition_query(item=item, db=db)


@router_car_base_info.post("/new_multiple_condition_query", summary="多条件查询")
def search_car_by_new_multiple_condition_query(item: schemas.CarBaseInfoNewMultipleConditionQuery,
                                               db: Session = Depends(get_db)):
    return crud.search_car_by_new_multiple_condition_query(item=item, db=db)


@router_car_base_info.post("/multiple_wheelbase", summary="获取轴距、轮距")
def get_multiple_wheelbase(item: schemas.MultipleWheelbase, db: Session = Depends(get_db)):
    return crud.get_multiple_wheelbase(item=item, db=db)
