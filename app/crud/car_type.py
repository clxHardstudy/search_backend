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


def get_car_type(db: Session):
    result: [models.CarType] = db.query(models.CarType).all()
    return result