# =========================
# 2. app/database.py (Connexion MongoDB)
# =========================

from pymongo import MongoClient

client = MongoClient("mongodb+srv://<username>:<password>@cluster.mongodb.net")
db = client.job_portal
users_collection = db.users
jobs_collection = db.jobs
applications_collection = db.applications
