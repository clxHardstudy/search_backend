from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


# 侧向力柔顺性(同向30mm拖距)
class LateralParallelThirtyMillMetersTrail(BaseModel):
    __tablename__ = "lateral_parallel_thirty_millmeters_trail"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    wc_compliance = Column(String(255), comment='轮心柔顺性')
    toe_compliance = Column(String(255), comment='前束角柔顺性')
    camber_compliance = Column(String(255), comment='外倾角柔顺性')
    lateral_stiffness_tcp = Column(String(255), comment='轮胎接地点侧向刚度 ')
    coordinate_system = Column(Integer,comment='坐标系【0：front、1：rear】')
    # car_type_id = Column(Integer, comment='车型类别id【1：轿车、2：SUV】')
    car_base_info_id = Column(Integer, comment="汽车主键id")