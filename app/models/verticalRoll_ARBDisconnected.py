from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 垂直侧倾工况(稳定杆断开)
class VerticalRollARBDisconnected(BaseModel):
    __tablename__ = "vertical_roll_arb_disconnected"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wheel_rate = Column(String(255), comment='悬架刚度')
    toe_angle_change = Column(String(255), comment='前束角变化')
    camber_change = Column(String(255), comment='外倾角变化')
    suspension_roll_stiffness = Column(String(255), comment='悬架侧倾刚度')
    total_vehicle_roll_stiffness = Column(String(255), comment='总侧倾刚度')
    roll_stiffness_distribution = Column(String(255), comment='侧倾刚度分配')
    kinematic_oll_centre_height = Column(String(255), comment='几何侧倾中心 ')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
