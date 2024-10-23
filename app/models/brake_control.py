from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Brake_control(BaseModel):
    __tablename__ = "brake_control"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    abs_module = Column(String(255), comment='ABS模块')
    epb = Column(String(255), comment="EPB")
    wheel_speed_sensor = Column(String(255), comment="轮速传感器")
    ipb = Column(String(255), comment="IPB")
    rbu = Column(String(255), comment="RBU")
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
