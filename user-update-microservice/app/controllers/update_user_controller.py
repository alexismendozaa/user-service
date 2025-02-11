from sqlalchemy.orm import Session
from app.models.user import User
import datetime

def update_user(db: Session, user_id: int, username: str = None, email: str = None, password: str = None):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "Usuario no encontrado"}

    update_data = {}

    if username is not None and user.username != username:
        update_data["username"] = username

    if email is not None and user.email != email:
        update_data["email"] = email

    if password is not None:
        update_data["password"] = password  # Se recomienda encriptar en el futuro

    if update_data:
        update_data["updatedAt"] = datetime.datetime.utcnow()  # Forzar actualización de updatedAt
        db.query(User).filter(User.id == user_id).update(update_data, synchronize_session=False)
        db.commit()  # Confirmar los cambios
        user = db.query(User).filter(User.id == user_id).first()  # Obtener el usuario actualizado
    
    return {"message": "Usuario actualizado con éxito", "user": {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "updatedAt": user.updatedAt
    }}
