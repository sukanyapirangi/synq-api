import os
from dotenv import load_dotenv

load_dotenv(override=True)


class Config:
    BASE_URL = os.getenv("BASE_URL", "http://localhost:8000/api")
    TIMEOUT = int(os.getenv("TIMEOUT", 300))
    UPLOAD_TIMEOUT = int(os.getenv("UPLOAD_TIMEOUT", 300))
    USERNAME = os.getenv("USERNAME", "")
    PASSWORD = os.getenv("PASSWORD", "")
