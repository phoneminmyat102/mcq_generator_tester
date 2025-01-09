from sqlalchemy import Column, Integer, Enum, ForeignKey
from db.database import Base

class ExamHistory(Base):
    __tablename__ = 'ExamHistory'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    section = Column(Enum('Morning', 'Afternoon'), nullable=False)
    given_mark = Column(Integer, nullable=False)
    got_mark = Column(Integer, nullable=False)
    result = Column(Enum('pass', 'fail'), nullable=False)
