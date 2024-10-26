from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 垂直平行工况(稳定杆连接)
class VerticalParallelARBConnected(BaseModel):
    __tablename__ = "vertical_parallel_arb_connected"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wheel_rate = Column(String(255), comment='悬架刚度')
    vertical_force_hysteresis = Column(String(255), comment='悬架摩擦')
    ride_frequency_no_tyre = Column(String(255), comment='固有频率（不包含轮胎）')
    ride_rate = Column(String(255), comment='行驶刚度')
    ride_frequency_with_tyre = Column(String(255), comment='固有频率（包含轮胎）')
    tyre_radial_rate = Column(String(255), comment='轮胎径向刚度')
    toe_angle_change = Column(String(255), comment='前束角变化')
    camber_change = Column(String(255), comment='外倾角变化')
    spin_angle_change = Column(String(255), comment='车轮转动变化')
    kinematic_oll_centre_height = Column(String(255), comment='几何侧倾中心')
    fore_aft_displacement_wc = Column(String(255), comment='轮心纵向位移 ')
    fore_aft_displacement_tcp = Column(String(255), comment='轮胎接地点纵向位移')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    # car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")