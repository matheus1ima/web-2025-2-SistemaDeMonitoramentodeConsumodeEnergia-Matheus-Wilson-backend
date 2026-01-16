from passlib.context import CryptContext
from jose import jwt, JWTError
from models import User
from fastapi import HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi import HTTPException

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = "ENERGIAZ_SUPER_SECRET_KEY"
ALGORITHM = "HS256"

def hash_password(password: str):
    password = password[:72]
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    plain = plain[:72]
    return pwd_context.verify(plain, hashed)

def create_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.utcnow() + timedelta(hours=24)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str, db):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        raise HTTPException(401, "Token inválido")

    user = db.query(User).filter(User.username == username).first()

    if not user:
        raise HTTPException(404, "Usuário não encontrado")

    return user

def get_bearer_token(authorization: str | None):
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization ausente")

    parts = authorization.split()

    if len(parts) != 2 or parts[0].lower() != "bearer":
        raise HTTPException(status_code=401, detail="Authorization deve ser: Bearer <token>")

    return parts[1]
