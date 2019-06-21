from sqlalchemy import (
    Column, Integer, SmallInteger, String, DateTime
)

from sqlalchemy.orm import relationship

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

    def __repr__(self):
        return 'email: %s | name: %s | is_active: %s' % (self.email, self.name, self.is_active)