from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class CarBaseInfo(BaseModel):
    __tablename__ = "car_base_info"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='车型名称', unique=True, nullable=False)
    wheelbase = Column(Integer, comment='轴距')
    front_track = Column(Integer, comment='前轮距')
    rear_track = Column(Integer, comment='后轮距')
    release_date = Column(Date, comment='发布日期')
    price_range = Column(String(255), comment='售价区间(万元）')
    curb_weight = Column(String(255), comment='整备质量（kg）')
    maximum_front_axle_mass = Column(String(255), comment='前轴最大质量（kg）')
    maximum_rear_axle_mass = Column(String(255), comment='后轴最大质量（kg）')
    create_time = Column(Integer, comment='创建时间')
    update_time = Column(Integer, comment='更新时间')
    car_type_id = Column(Integer, comment="车型类别 1：轿车、2：SUV")
    platform_id = Column(Integer, comment="所属平台 1：T1X、2：T2X")
