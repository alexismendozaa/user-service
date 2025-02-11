from sqlalchemy.orm import Session
from app.models.user import User

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
        return {"message": "Usuario eliminado con éxito"}
    return {"error": "Usuario no encontrado"}
