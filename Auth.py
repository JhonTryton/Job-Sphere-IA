# =========================
# 4. app/routers/auth.py (Authentification)
# =========================

from fastapi import APIRouter, HTTPException
from database import users_collection
from models import User

router = APIRouter(prefix="/auth")

@router.post("/register")
def register(user: User):
    if users_collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email already registered")
    users_collection.insert_one(user.dict())
    return {"message": "User registered successfully"}

@router.post("/login")
def login(data: dict):
    user = users_collection.find_one({"email": data["email"], "password": data["password"]})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"message": "Login successful"}
    
