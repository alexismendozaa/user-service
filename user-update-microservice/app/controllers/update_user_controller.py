from sqlalchemy.orm import Session
from app.models.user import User

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "Usuario no encontrado"}

    update_data = {}
    
    if username and user.username != username:
        update_data["username"] = username

    if email and user.email != email:
        update_data["email"] = email

    if update_data:
        db.query(User).filter(User.id == user_id).update(update_data)
        db.commit()
        user = db.query(User).filter(User.id == user_id).first()  # Obtener el usuario actualizado
    
    return {"message": "Usuario actualizado con éxito", "user": user}
