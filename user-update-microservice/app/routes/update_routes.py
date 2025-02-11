from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.db_service import get_db
from app.controllers.update_user_controller import update_user

router = APIRouter()

@router.put("/users/{user_id}")
def update_user_endpoint(user_id: int, username: str = None, email: str = None, password: str = None, db: Session = Depends(get_db)):
    result = update_user(db, user_id, username, email, password)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
