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

ACCESS_TOKEN_EXPIRE_MINUTES = config.get('token', 'expire_minutes')
LOGIN_EXPIRED = int(config.get('token', 'login_expired'))
PING_INTERVAL = int(config.get('token', 'ping_interval'))
USER_MAX_COUNT = int(config.get('token', 'user_max_count'))
MAX_TIME_PING = int(config.get('token', 'max_time_ping'))


def create_user(db: Session, item: schemas.UserCreate):
    res: models.User = db.query(models.User).filter(models.User.username == item.username).first()
    if res:
        # raise Exception(f"用户 {item.username} 已存在")
        print(f"用户{item.username}已存在")
        return {"exist": "True"}
    password = item.password
    db_item = models.User(**{
        'username': item.username,
        'password_hash': get_password_hash(password),
        "create_time": int(time.time()),
        "update_time": int(time.time()),
        "last_login": int(time.time()),
    })
    db_item.auth_token = create_access_token(db_item.id, 'user')
    db.add(db_item)
    db.commit()
    db.flush()
    res = db_item.to_dict()
    res.update({"exist": "False"})
    print(res)
    return res


def login_user_swagger(db: Session, item: schemas.UserSwaggerLogin):
    user: models.User = db.query(models.User).filter(models.User.username == item.username).first()
    # 用户不存在
    if not user:
        raise Exception(404, f"用户 {item.username} 不存在")
    # 密码错误
    if not verify_password(item.password, user.password_hash):
        raise Exception(401, "用户密码错误")
    auth_token = create_access_token(user.id, 'user')
    user.auth_token = auth_token
    # 如果该用户还未登陆过，表中字段不存在json字符串
    user.last_login = int(time.time())
    db.commit()
    db.flush()
    return {"access_token": user.auth_token, "token_type": "bearer", "user_id": user.id,
            "user_name": user.username}


def login_user(db: Session, item: schemas.UserLogin):
    user: models.User = db.query(models.User).filter(models.User.username == item.username).first()
    # 用户不存在
    if not user:
        return {"status_code": 404}
    # 密码错误
    if not verify_password(item.password, user.password_hash):
        return {"status_code": 401}
    user.last_login = int(time.time())
    db.commit()
    db.flush()
    res = user.to_dict()
    res.update({"status_code": 200})
    print(res)
    return res


def update_user(db: Session, item_id: int, update_item: schemas.UserUpdate):
    user: models.User = db.query(models.User).filter(models.User.id == item_id).first()
    if not user:
        raise Exception("用户不存在")
    now = int(time.time())
    user.update_time = now
    user.password_hash = get_password_hash(update_item.password)
    db.commit()
    db.flush()
    return user.to_dict()


def get_user_once(db: Session, item_id: int):
    res: models.User = db.query(models.User).filter(models.User.id == item_id).first()
    return res


def get_user_once_by_name(db: Session, name: str):
    res: models.User = db.query(models.User).filter(models.User.name == name).first()
    return res


def get_users(db: Session):
    query = db.query(models.User).all()
    return query


def delete_user(db: Session, item_id: int):
    item = get_user_once(item_id=item_id, db=db)
    if not item:
        raise Exception(404, f"删除失败, 用户 {item_id} 不存在")
    db.delete(item)
    db.commit()
    db.flush()
    return True


async def check_alive(websocket, db, token):
    await websocket.accept()
    retry = 0
    sub, exp, type = check_access_token(token, "user")  # user_id 过期时间 type字段
    user: models.User = db.query(models.User).filter(models.User.id == sub).first()
    # 如果还在连接状态
    while websocket.application_state.value == 1:
        try:
            await websocket.send_text('1')
            print("发送消息：1")
            recv_data = await asyncio.wait_for(websocket.receive_text(), 15)
            print("接收消息：{}".format(recv_data))
            if recv_data == "2":
                if websocket.application_state.value == 1:
                    await websocket.close()
                break
            if recv_data == "0":
                print("接收到消息：{}".format(recv_data))
                print("用户请求主动退出登陆...")
                retry = 0
                print("正在准备清除用户token...")
                clear_token(db, token, sub)
                if websocket.application_state.value == 1:
                    await websocket.close()
                break
            if type == "pass":
                print("type = pass,无需校验！")
                retry = 0
                continue
            elif type == "check":
                retry = 0
                update_last_ping(db, token, user)
                continue
        # 心跳异常：断开连接，清除token，更新last_ping
        except Exception as e:
            retry += 1
            print(f'websocket 心跳异常: retry={retry}, user={user.name},e:{str(e)}')
            if retry >= LOGIN_EXPIRED // PING_INTERVAL:
                print(f'{retry}次心跳失败,websocket关闭,user={user.name},exception:{str(e)}')
                if websocket.application_state.value == 1:
                    clear_token(db, token, sub)
                if websocket.application_state.value == 1:
                    await websocket.close()
                break


# 过期token清除：用户长时间没有ping就清除
def stop_ping_clear_token(db: Session, user_id: int):
    user: models.User = db.query(models.User).filter(models.User.id == user_id).first()
    auth_token_list_dic = []
    if user.auth_token_json is not None and user.auth_token_json != "":
        auth_token_list_dic = json.loads(user.auth_token_json)
    for index, auth_token_dic in enumerate(auth_token_list_dic):
        if auth_token_dic.get("last_ping") is not None and int(time.time()) - int(
                auth_token_dic.get("last_ping")) > MAX_TIME_PING:
            auth_token_list_dic.pop(index)
    user.auth_token_json = json.dumps(auth_token_list_dic)
    db.commit()
    db.refresh(user)
    return user


def update_last_ping(db: Session, token: str, user: models.User):
    auth_token_list_dic = json.loads(user.auth_token_json)
    for index, auth_token_dic in enumerate(auth_token_list_dic):
        if auth_token_dic.get("auth_token") == token:
            auth_token_list_dic[index].update({"last_ping": int(time.time())})
            user.auth_token_json = json.dumps(auth_token_list_dic)
            db.commit()
            db.flush()
            break


def clear_token(db: Session, token: str, sub: int):
    res = db.query(models.User).filter(models.User.id == sub).first()
    auth_token_list_dic = json.loads(res.auth_token_json)
    for index, auth_token_dic in enumerate(auth_token_list_dic):
        if auth_token_dic.get("auth_token") == token:
            # 清除token
            auth_token_list_dic.pop(index)
            res.auth_token_json = json.dumps(auth_token_list_dic)
            db.commit()
            db.flush()
            break
