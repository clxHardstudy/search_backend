from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class CarBaseInfo(BaseModel):
    __tablename__ = "car_base_info"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='车型名称', unique=True, nullable=False)
    wheelbase = Column(Integer, comment='轴距')
    release_date = Column(Date, comment='发布日期')
    create_time = Column(Integer, comment='创建时间')
    update_time = Column(Integer, comment='更新时间')
    car_type_id = Column(Integer, comment="1：轿车、2：SUV")
