from sqlalchemy import (
    Column, String, Text, Integer, SmallInteger, DateTime
)

from app import Base

class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime)
    created_by = Column(Integer)
    updated_at = Column(DateTime)
    updated_by = Column(Integer)
    is_published = Column(SmallInteger)