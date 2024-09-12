import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.database import Base, engine
from app.routers.user import router_user
from app.routers.cartype import router_cartype
from configs.setting import config

Base.metadata.create_all(bind=engine)

app = FastAPI(title="工程实践")

# CORS 跨源资源共享
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 设置允许的源，可以是具体的域名，也可以是通配符"*"表示允许所有来源
    allow_methods=["*"],  # 设置允许的HTTP方法
    allow_headers=["*"],  # 设置允许的HTTP头部
    allow_credentials=True,  # 允许发送凭据（例如：cookies）
)


@app.get("/", tags=["主页"])
def get_home():
    return "hello,welcome!"


app.include_router(router_user)
app.include_router(router_cartype)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
