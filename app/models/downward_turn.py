from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Downward_turn(BaseModel):
    __tablename__ = "downward_turn"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    mechanical_steering_gear = Column(String(255), comment='机械转向器')
    dp_eps = Column(String(255), comment='双小齿轮式电动助力转向器')
    r_eps = Column(String(255), comment='齿条式电动助力转向')
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
