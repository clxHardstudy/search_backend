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
from configs.setting import config


def get_vertical_parallel_arb_connected(db: Session):
    result: [models.VerticalParallelARBConnected] = db.query(models.VerticalParallelARBConnected).all()
    return result


def get_vertical_parallel_arb_connected_by_car_type_id(item_id: int, db: Session):
    result: [models.VerticalParallelARBConnected] = db.query(
        models.VerticalParallelARBConnected).filter(models.VerticalParallelARBConnected.car_type_id == item_id).all()
    print(len(result))
    return result
