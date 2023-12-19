from sqlalchemy import Column, String, Integer

from ..database import Base

class Fruit(Base):
    __tablename__ = "fruits"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)