from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from ..models.user_model import User

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/")
async def get_all_users(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User))

    users = result.scalars()

    if not users:
        raise

    return users
