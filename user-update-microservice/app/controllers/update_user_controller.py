from sqlalchemy.orm import Session
from app.models.user import User

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return {"error": "Usuario no encontrado"}

    updated = False  # Flag para saber si hubo cambios

    if username and user.username != username:
        user.username = username
        updated = True

    if email and user.email != email:
        user.email = email
        updated = True

    if updated:
        db.commit()  # Guardar solo si hubo cambios
        db.refresh(user)  # Asegurar que los datos reflejan la BD

    return {"message": "Usuario actualizado con éxito", "user": user}

