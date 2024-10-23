from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Brake_execution(BaseModel):
    __tablename__ = "brake_execution"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    front_brake_disc = Column(String(255), comment='前制动盘')
    rear_brake_disc = Column(String(255), comment='后制动盘')
    rear_brake_drum = Column(String(255), comment="后制动鼓")
    front_calipers = Column(String(255), comment="前卡钳")
    rear_calipers = Column(String(255), comment="后卡钳")
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
