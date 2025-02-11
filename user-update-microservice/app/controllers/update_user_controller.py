from sqlalchemy.orm import Session
from app.models.user import User
import datetime

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "Usuario no encontrado"}

    # Actualizar solo los campos que se proporcionan en la solicitud
    if username:
        user.username = username
    if email:
        user.email = email

    # Asegurar que `updatedAt` se actualiza siempre
    user.updatedAt = datetime.datetime.utcnow()

    db.commit()  # Guardar los cambios en la base de datos
    db.refresh(user)  # Refrescar la instancia con los valores nuevos desde la BD

    return {"message": "Usuario actualizado con éxito", "user": {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "createdAt": user.createdAt,
        "updatedAt": user.updatedAt
    }}
