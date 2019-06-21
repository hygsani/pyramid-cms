from sqlalchemy import (
    Column, String, Text, Integer, SmallInteger, DateTime,
    ForeignKey
)

from sqlalchemy.orm import relationship, backref

from app import Base

class Post(Base):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(Text)
    created_at = Column(DateTime)
    created_by = Column(Integer, ForeignKey('users.user_id'))
    updated_at = Column(DateTime)
    updated_by = Column(Integer, ForeignKey('users.user_id'))
    is_published = Column(SmallInteger)
    created_by_user = relationship('User', foreign_keys=[created_by])
    updated_by_user = relationship('User', foreign_keys=[updated_by])


    def __repr__(self):
        return 'title: %s | content: %s | is_published: %s | created_at: %s' % (
            self.title, self.content, self.is_published, self.created_at
        )