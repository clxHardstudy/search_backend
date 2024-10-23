from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Transmission(BaseModel):
    __tablename__ = "transmission"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    transmission_shaft = Column(String(255), comment='传动轴')
    drive_shaft = Column(String(255), comment='驱动轴')
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
