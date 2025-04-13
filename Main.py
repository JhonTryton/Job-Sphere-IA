# =========================
# 1. app/main.py (Lanceur principal avec FastAPI et uvicorn)
# =========================

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import auth, jobs, applications, user

app = FastAPI(title="AI Job Application Portal")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(jobs.router)
app.include_router(applications.router)
app.include_router(user.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Job Application Portal!"}
