from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


# 悬架结构件
class Structural_Parts(BaseModel):
    __tablename__ = "structural_parts"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    subframe = Column(String(255), comment='副车架')
    front_upper_control_arm = Column(String(255), comment="前上控制臂")
    rear_upper_control_arm = Column(String(255), comment="后上控制臂")
    front_down_control_arm = Column(String(255), comment="前下控制臂")
    rear_down_control_arm = Column(String(255), comment="后下控制臂")
    front_arm = Column(String(255), comment="前束臂")
    coordinate_system = Column(Integer, comment='模块【0：front、1：rear】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
