from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 纵向制动工况
class LongitudinalBraking(BaseModel):
    __tablename__ = "longitudinal_braking"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wc_compliance = Column(String(255), comment='轮心柔顺性')
    toe_compliance = Column(String(255), comment='前束角柔顺性')
    camber_compliance = Column(String(255), comment='外倾角柔顺性')
    spin_angle_change = Column(String(255), comment='车轮转动变化')
    longitudinal_stiffness_tcp = Column(String(255), comment='轮胎接地点纵向刚度')
    anti_lift_or_squat_angle = Column(String(255), comment='抗举升/后座角')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    # car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
