from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class Modules(BaseModel):
    __tablename__ = "modules"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='模块：K&C｜前悬架｜后悬架...', unique=True, nullable=False)
    name_en = Column(String(255), comment='模块：KC｜front_suspension｜rear_suspension...', unique=True, nullable=False)
