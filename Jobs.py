# =========================
# 5. app/routers/jobs.py (Recherche d'emploi avec scraping simplifié)
# =========================

from fastapi import APIRouter
from database import jobs_collection
from models import Job

router = APIRouter(prefix="/jobs")

@router.post("/add")
def add_job(job: Job):
    jobs_collection.insert_one(job.dict())
    return {"message": "Job added"}

@router.get("/all")
def get_all_jobs():
    return list(jobs_collection.find({}, {"_id": 0}))
