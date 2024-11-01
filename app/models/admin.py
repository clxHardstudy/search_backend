from sqlalchemy import Column, Integer, String, JSON

from app.models.database import BaseModel


class Admin(BaseModel):
    __tablename__ = "admin"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='用户类别', unique=True)
    name_en = Column(String(255), comment='用户类别英文', unique=True)


