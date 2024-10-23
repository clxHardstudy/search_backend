import copy
import json
import time
import asyncio
import anyio
import websockets.exceptions
from fastapi import Depends
from app import models, schemas, get_db
from sqlalchemy.orm import Session
from app.common.validation import get_password_hash, create_access_token, verify_password, TokenSchemas, \
    check_access_token, check_user
import pandas as pd


def data_import(db: Session, data_frame: pd.DataFrame):
    # 读取第六列的数据
    data_dic = data_frame.iloc[:, 2]  # 第六列的索引是 5 (因为索引从 0 开始)
    # first_row_data = data_frame.iloc[2, :]  # 第六列的索引是 5 (因为索引从 0 开始)
    # 打印或处理第六列的数据
    return data_dic
