from sqlalchemy.orm import Session
from app.models.user import User
import datetime

def update_user(db: Session, user_id: int, username: str = None, email: str = None, password: str = None):
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        return {"error": "Usuario no encontrado"}

    updated = False  # Bandera para saber si hubo cambios

    if username is not None and user.username != username:
        user.username = username
        updated = True

    if email is not None and user.email != email:
        user.email = email
        updated = True

    if password is not None:
        user.password = password  # Se recomienda encriptar antes de almacenar
        updated = True

    if updated:
        user.updatedAt = datetime.datetime.utcnow()
        db.commit()  # Confirmar los cambios en la base de datos
        db.refresh(user)  # Refrescar la instancia con los valores nuevos

    return {"message": "Usuario actualizado con éxito", "user": {
        "id": user.id,
        "username": user.username,
        "email": user.email,
        "password": user.password,  # Solo para pruebas, deberías ocultarlo en producción
        "updatedAt": user.updatedAt
    }}
