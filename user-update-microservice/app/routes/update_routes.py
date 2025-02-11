from fastapi import APIRouter, HTTPException
from app.controllers.update_user_controller import update_user

router = APIRouter()

@router.put("/users/{user_id}")
def update_user_endpoint(user_id: int, username: str = None, email: str = None, password: str = None):
    result = update_user(user_id, username, email, password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
