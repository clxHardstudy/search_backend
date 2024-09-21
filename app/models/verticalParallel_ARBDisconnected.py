from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 垂直平行工况(稳定杆断开)
class VerticalParallelARBDisconnected(BaseModel):
    __tablename__ = "vertical_parallel_arb_disconnected"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wheel_rate = Column(String(255), comment='悬架刚度')
    vertical_force_hysteresis = Column(String(255), comment='悬架摩擦')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
