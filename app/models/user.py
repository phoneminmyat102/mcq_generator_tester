from sqlalchemy import Column, Integer, String
from db.database import Base

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    name = Column(String(255), nullable=False)
