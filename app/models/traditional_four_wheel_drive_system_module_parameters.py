from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class TraditionalFourWheelDriveSystemModuleParameters(BaseModel):
    __tablename__ = "traditional_four_wheel_drive_system_module_parameters"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='传动四驱系统子表【中文】', unique=True, nullable=False)
    name_en = Column(String(255), comment='传动四驱系统子表【英文】', unique=True, nullable=False)
