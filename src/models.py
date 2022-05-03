import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    likes = Column(String(250), nullable=False)
    likes = relationship('Likes')
    likes_id = Column(Integer, ForeignKey('likes.id'))
    dislikes = Column(String(250), nullable=False)
    comments = Column(String(250), nullable=False)
    comments = relationship('Comment')
    comments_id = Column(Integer, ForeignKey('comment.id'))
    image = Column(String(250), nullable=False)
    image = relationship('Images')
    image_id = Column(Integer, ForeignKey('image.id'))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(String(250), ForeignKey('post.id'), nullable=False)

    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey("user.id"))
    user_to_id = Column(Integer, ForeignKey("user.id"))


class Comment(Base):
    id = Column(Integer, primary_key=True)
    __tablename__ = 'Comment'
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User')
    comments = Column(String(500))
    post_id = Column(Integer, ForeignKey('post.id'))
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')