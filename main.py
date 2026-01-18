from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.database.session import get_db, init_db
from src.database.models import Users

app = FastAPI()


@app.on_event("startup")
async def startup():
    await init_db()


@app.get("/")
async def hello_world(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Users))
    users = result.scalars().all()
    return {"users": users}
