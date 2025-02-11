from sqlalchemy.orm import Session
from app.models.user import User
import datetime

def update_user(db: Session, user_id: int, username: str = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first()
    
    if not user:
        return {"error": "Usuario no encontrado"}

    update_data = {}
    
    if username and user.username != username:
        update_data["username"] = username

    if email and user.email != email:
        update_data["email"] = email

    # ⚠️ Asegurar que el campo updatedAt también se actualice manualmente
    update_data["updatedAt"] = datetime.datetime.utcnow()

    if update_data:
        db.query(User).filter(User.id == user_id).update(update_data, synchronize_session=False)
        db.commit()
    
    user = db.query(User).filter(User.id == user_id).first()  # Volver a obtener el usuario actualizado
    return {"message": "Usuario actualizado con éxito", "user": user}
