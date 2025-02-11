from sqlalchemy.orm import Session
from app.models.user import User

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "Usuario no encontrado"}

    if username:
        user.username = username
    if email:
        user.email = email

    db.commit()
    db.refresh(user)
    return {"message": "Usuario actualizado con éxito", "user": user}
