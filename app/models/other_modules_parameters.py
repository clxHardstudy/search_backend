from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class OtherModulesParameters(BaseModel):
    __tablename__ = "other_modules_parameters"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='其他模块参数中文', unique=True, nullable=False)
    name_en = Column(String(255), comment='其他模块参数英文', unique=True, nullable=False)
