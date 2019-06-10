from sqlalchemy import (
    Column, Integer, SmallInteger, String, DateTime
)

from app import Base

class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    email = Column(String)
    name = Column(String)
    password = Column(String)
    is_active = Column(SmallInteger)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)