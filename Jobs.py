## 💼 `app/jobs.py'python
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database import jobs, applications
from datetime import datetime

router = APIRouter()

class Job(BaseModel):
    title: str
    company: str
    email: str
    deadline: str
    location: str
    size: int

@router.post("/add-job")
async def add_job(job: Job):
    await jobs.insert_one(job.dict())
    return {"msg": "Job added"}

@router.get("/jobs")
async def get_jobs():
    today = datetime.today().isoformat()
    cursor = jobs.find({"deadline": {"$gte": today}}).sort("size")
    return [job async for job in cursor]

@router.post("/apply/{job_id}")
async def apply_job(job_id: str, user_email: str):
    job = await jobs.find_one({"_id": job_id})
    if not job:
        raise HTTPException(404, "Job not found")
    await applications.insert_one({"user": user_email, "job": job})
    return {"message": "Applied successfully"}

@router.get("/applied/{user_email}")
async def get_applied(user_email: str):
    apps = applications.find({"user": user_email})
    return [app async for app in apps]
  
