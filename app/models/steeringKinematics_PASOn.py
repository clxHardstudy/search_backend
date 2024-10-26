from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 转向运动学(发动机启动)
class SteeringKinematicsPASOn(BaseModel):
    __tablename__ = "steering_kinematics_pas_on"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    overall_steer_ratio = Column(String(255), comment='总传动比 (+/-360°)')
    on_center_steer_ratio = Column(String(255), comment='中间位置传动比 (+/-20 °)')
    steering_friction = Column(String(255), comment='转向摩擦 ')
    scrub_radius = Column(String(255), comment='摩擦半径')
    mechanical_trail = Column(String(255), comment='机械拖距')
    kingpin_offset_pl = Column(String(255), comment='地面处主销偏置距')
    kingpin_offset_wc = Column(String(255), comment='轮心处主销偏置距')
    castor_angle = Column(String(255), comment='主销后倾角')
    kingpin_inclination_angle = Column(String(255), comment='主销内倾角')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    # car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")