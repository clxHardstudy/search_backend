from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 侧向力柔顺性(反向)
class LateralParallelOutOfPhase(BaseModel):
    __tablename__ = "lateral_parallel_out_of_phase"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wc_compliance = Column(String(255), comment='轮心柔顺性')
    toe_compliance = Column(String(255), comment='前束角柔顺性')
    camber_compliance = Column(String(255), comment='外倾角柔顺性')
    lateral_stiffness_tcp = Column(String(255), comment='轮胎接地点侧向刚度 ')
    force_roll_centre_height = Column(String(255), comment='力侧倾中心高度')
    coordinate_system = Column(Integer, comment='坐标系【0：front、1：rear】')
    # car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")
