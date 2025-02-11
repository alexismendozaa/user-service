from sqlalchemy.orm import Session
from app.models.user import User

def get_user_by_id(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    return user

def get_all_users(db: Session):
    return db.query(User).all()
