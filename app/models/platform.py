from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class Platform(BaseModel):
    __tablename__ = "platform"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='平台类别：【T1X、T2X】', unique=True, nullable=False)
