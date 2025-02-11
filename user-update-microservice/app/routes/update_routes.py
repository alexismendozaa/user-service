from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, Field
from app.controllers.update_user_controller import update_user

router = APIRouter()

# Definir el esquema que FastAPI usará para validar los datos de entrada
class UpdateUserRequest(BaseModel):
    username: str = Field(None, example="Kafka")
    email: str = Field(None, example="nuevo_correo@example.com")
    password: str = Field(None, example="kafka123")

@router.put("/users/{user_id}")
def update_user_endpoint(user_id: int, user_data: UpdateUserRequest):
    result = update_user(user_id, user_data.username, user_data.email, user_data.password)
    if "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])
    return result
