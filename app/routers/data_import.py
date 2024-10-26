import time
from io import BytesIO

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
from app import schemas, crud
from fastapi import APIRouter, WebSocket, Depends, UploadFile, File
from app.common.validation import TokenSchemas, OAuth2PasswordRequestForm, check_user, check_user_ws, \
    fromat_token_to_user
from app import get_db, models
import pandas as pd
import numpy as np

from configs.setting import config

router_data_import = APIRouter(
    prefix="/data_import",
    tags=["data_import-数据导入"],
)


@router_data_import.post("/", summary="数据导入")
async def data_import(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # 读取上传的 Excel 文件
    contents = await file.read()
    # 将字节流转换为 Pandas DataFrame
    df = pd.read_excel(BytesIO(contents))
    return crud.data_import(db=db, df=df)
