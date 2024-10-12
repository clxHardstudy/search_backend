from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 回正力矩柔顺性（同向）
class AligningTorqueParallel(BaseModel):
    __tablename__ = "aligning_torque_parallel"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    toe_compliance = Column(String(255), comment='前束角柔顺性')
    camber_compliance = Column(String(255), comment='外倾角柔顺性')
    coordinate_system = Column(Integer,comment='坐标系【0：front、1：rear】')
    car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")

