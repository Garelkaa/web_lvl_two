from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    gender = Column(String)
    status = Column(String)
    posts = relationship("Post", back_populates="user")


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    title = Column(String)
    body = Column(String)
    user = relationship("User", back_populates="posts")
