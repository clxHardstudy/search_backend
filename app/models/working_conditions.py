from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class WorkingConditions(BaseModel):
    __tablename__ = "working_conditions"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='工况表名', unique=True, nullable=False)
    name_en = Column(String(255), comment='工况表名【英文】', unique=True, nullable=False)
    kc_parameters_id_list = Column(JSON, comment='工况性能参数列表')
