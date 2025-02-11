from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.db_service import get_db
from app.controllers.select_user_controller import get_user_by_id, get_all_users

router = APIRouter()

@router.get("/users/{user_id}")
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

@router.get("/users")
def get_all_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)
