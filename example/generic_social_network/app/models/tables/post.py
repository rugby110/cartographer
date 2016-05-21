from copy import copy

from generic_social_network.app import db
from sqlalchemy import Column, Integer, ForeignKey, String, Text


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = Column(Integer, primary_key=True, nullable=False)
    author_id = Column(Integer, ForeignKey("users.user_id"), index=True, nullable=False)
    title = Column(String(512), default='')
    body = Column(Text)