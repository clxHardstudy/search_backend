from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Elastic_Parts(BaseModel):
    __tablename__ = "elastic_parts"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    shock_absorbers = Column(String(255), comment='减震器')
    spring = Column(String(255), comment="弹簧")
    stabilizer_bar = Column(String(255), comment="稳定杆")
    connecting_rod = Column(String(255), comment="连接杆")
    bushing = Column(String(255), comment="衬套")
    ball_pin = Column(String(255), comment="球销")
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
