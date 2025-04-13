# =========================
# 6. app/routers/applications.py (Postulation avec IA et emailing)
# =========================

from fastapi import APIRouter
from database import applications_collection
from models import Application
from utils.emailer import send_email
from utils.ia_writer import generate_cover_letter

router = APIRouter(prefix="/applications")

@router.post("/apply")
def apply(application: Application):
    cover = generate_cover_letter(application.user_email, application.job_id)
    send_email(application.user_email, application.job_id, application.cv_link, cover)
    applications_collection.insert_one(application.dict())
    return {"message": "Application sent successfully"}
