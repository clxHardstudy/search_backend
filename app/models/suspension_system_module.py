from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class SuspensionSystemModule(BaseModel):
    __tablename__ = "suspension_system_module"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='悬架系统子表【中文】', unique=True, nullable=False)
    name_en = Column(String(255), comment='悬架系统子表【英文】', unique=True, nullable=False)
    suspension_system_module_parameters_id_list = Column(JSON, comment='悬架系统子表参数列表')
