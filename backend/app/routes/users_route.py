from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from ..repositories import user_repository
from ..schemas.user_schemas import UserCreate

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/")
async def get_users(db: AsyncSession = Depends(get_db)):
    return await user_repository.get_all_users(db)

@user_router.get("/{user_id}")
async def get_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    return await user_repository.get_user_by_id(user_id, db)

@user_router.post("/create")
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await user_repository.create_user(user, db)

