from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class Upward_turn(BaseModel):
    __tablename__ = "upward_turn"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    steering_column = Column(String(255), comment='转向管柱')
    electric_power_steering_column = Column(String(255), comment='电动助力转向管柱')
    electric_adjustable_steering_column = Column(String(255), comment='电动可调转向管柱')
    electric_adjustable_power_steering_column = Column(String(255), comment='电动可调助力转向管柱')
    intermediate_shaft_assembly = Column(String(255), comment='中间轴总成')
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
