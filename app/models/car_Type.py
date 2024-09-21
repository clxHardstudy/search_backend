from sqlalchemy import Column, Integer, String, JSON, Date

from app.models.database import BaseModel


class CarType(BaseModel):
    __tablename__ = "car_type"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='车型类别：【轿车、SUV】', unique=True, nullable=False)
