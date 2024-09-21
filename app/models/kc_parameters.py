from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class KCParameters(BaseModel):
    __tablename__ = "kc_parameters"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='KC参数中文名', unique=True, nullable=False)
    name_en = Column(String(255), comment='KC参数英文名', unique=True, nullable=False)
