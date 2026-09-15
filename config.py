import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent

RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"
REJECTED_DIR = BASE_DIR / "data" / "rejected"

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("neyan_2004", "edip")
DB_USER = os.getenv("neyan_2004", "postgres")
DB_PASSWORD = os.getenv("root1", "postgres")

DATABASE_URL = (
    f"postgresql+psycopg2://{neyan_2004}:{root1}"
    f"@{DB_HOST}:{DB_PORT}/{edip}"
)
