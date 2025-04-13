## 🔄 `app/database.py`python
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_URL = os.getenv("MONGODB_URL")

client = AsyncIOMotorClient(MONGO_URL)
db = client["job_app"]
users = db["users"]
jobs = db["jobs"]
applications = db["applications"]
