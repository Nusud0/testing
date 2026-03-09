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
async def get_users():
    return user_repository.get_all_users()

@user_router.post("/create")
async def get_users(user: UserCreate):
    return user_repository.create_user(user)