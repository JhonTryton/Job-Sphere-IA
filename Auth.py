## 🔐 `app/auth.py`python
from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel, EmailStr
from passlib.context import CryptContext
from jose import jwt
import os
from app.database import users

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

class User(BaseModel):
    email: EmailStr
    password: str

@router.post("/register")
async def register(user: User):
    if await users.find_one({"email": user.email}):
        raise HTTPException(400, "Email already registered")
    hash_pwd = pwd_context.hash(user.password)
    await users.insert_one({"email": user.email, "password": hash_pwd})
    return {"message": "User registered"}

@router.post("/login")
async def login(user: User):
    u = await users.find_one({"email": user.email})
    if not u or not pwd_context.verify(user.password, u['password']):
        raise HTTPException(401, "Invalid credentials")
    token = jwt.encode({"sub": user.email}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token}
  
