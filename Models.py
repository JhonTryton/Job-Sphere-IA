# =========================
# 3. app/models.py (Schemas Pydantic)
# =========================

from pydantic import BaseModel, EmailStr
from typing import Optional, List

class User(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str

class Job(BaseModel):
    title: str
    company: str
    location: str
    deadline: str
    email: EmailStr
    description: str

class Application(BaseModel):
    user_email: EmailStr
    job_id: str
    cover_letter: str
    cv_link: str
