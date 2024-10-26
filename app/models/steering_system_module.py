from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class SteeringSystemModule(BaseModel):
    __tablename__ = "steering_system_module"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='转向系统子表【中文】', unique=True, nullable=False)
    name_en = Column(String(255), comment='转向系统子表【英文】', unique=True, nullable=False)
    steering_system_module_parameters_id_list = Column(JSON, comment='转向系统子表参数列表')
