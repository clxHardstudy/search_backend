from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class SuspensionSystemModuleParameters(BaseModel):
    __tablename__ = "suspension_system_module_parameters"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='悬架系统模块参数【中文名】', unique=True, nullable=False)
    name_en = Column(String(255), comment='悬架系统模块参数【英文名】', unique=True, nullable=False)
