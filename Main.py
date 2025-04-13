## 📁 `app/main.py python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import auth, jobs

app = FastAPI()

origins = ["*"]
app.add_middleware(CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(auth.router)
app.include_router(jobs.router)

@app.get("/")
def root():
    return {"msg": "Job App AI Tool is running"}
