from sqlalchemy.orm import Session
from app.models.user import User
import datetime

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "Usuario no encontrado"}

    updated = False  # Flag para verificar si se realizaron cambios

    if username and user.username != username:
        user.username = username
        updated = True

    if email and user.email != email:
        user.email = email
        updated = True

    # Asegurar que updatedAt siempre se actualiza
    if updated:
        user.updatedAt = datetime.datetime.utcnow()
        db.commit()  # Confirmar cambios en la base de datos
        db.refresh(user)  # Refrescar la instancia con los valores nuevos

    return {"message": "Usuario actualizado con éxito", "user": user}
