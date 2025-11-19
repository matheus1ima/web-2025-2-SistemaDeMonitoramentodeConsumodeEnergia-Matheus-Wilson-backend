from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/login", tags=["Login"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/")
def login(data: LoginRequest):
    if data.username == "admin" and data.password == "admin":
        return {"access_token": "fake-jwt-token", "token_type": "bearer"}
    else:
        raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
