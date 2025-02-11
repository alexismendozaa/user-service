from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.db_service import get_db
from app.controllers.delete_user_controller import delete_user

router = APIRouter()

@router.delete("/users/{user_id}")
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    result = delete_user(db, user_id)
    if "error" in result:
        raise HTTPException(status_code=404, detail=result["error"])
    return result
