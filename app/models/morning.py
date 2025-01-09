from sqlalchemy import Column, Integer, String, Enum, Text
from db.database import Base

class Morning(Base):
    __tablename__ = 'Morning'

    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    option_a = Column(String(255), nullable=False)
    option_b = Column(String(255), nullable=False)
    option_c = Column(String(255), nullable=False)
    option_d = Column(String(255), nullable=False)
    type = Column(Enum('1', '2', '3'), nullable=False)
    answer = Column(Enum('a', 'b', 'c', 'd'), nullable=False)
