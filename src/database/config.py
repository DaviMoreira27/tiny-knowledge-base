import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

load_dotenv()

REQUIRED_VARS = [
    "DB_USER",
    "DB_PASS",
    "DB_HOST",
    "DB_PORT",
    "DB_NAME",
]

missing = [v for v in REQUIRED_VARS if not os.getenv(v)]
if missing:
    raise RuntimeError(f"Missing env vars: {', '.join(missing)}")

DATABASE_URL = URL.create(
    drivername="postgresql+asyncpg",
    username=os.environ["DB_USER"],
    password=os.environ["DB_PASS"],
    host=os.environ["DB_HOST"],
    port=int(os.environ["DB_PORT"]),
    database=os.environ["DB_NAME"],
)

print(DATABASE_URL)