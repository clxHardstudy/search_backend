from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class Suspension(BaseModel):
    __tablename__ = "suspension"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    front_suspension = Column(String(255), comment='前悬置')
    rear_suspension = Column(String(255), comment='后悬置')
    left_suspension = Column(String(255), comment='左悬置')
    right_suspension = Column(String(255), comment='右悬置')
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
