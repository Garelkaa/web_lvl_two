from sqlalchemy.orm import Session
from .models import User, Post


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_posts_by_user_id(db: Session, user_id: int):
    return db.query(Post).filter(Post.user_id == user_id).all()
