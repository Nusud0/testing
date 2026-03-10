from fastapi import APIRouter, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from ..services.user_service import UserService
from ..schemas.user_schemas import UserListResponse, UserResponse, UserCreate

user_router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@user_router.get("/", response_model=UserListResponse, status_code=status.HTTP_200_OK)
async def get_users(db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return service.get_all_users()

@user_router.get("/{user_id}", response_model=UserResponse, status_code=status.HTTP_200_OK)
async def get_user_id(user_id: int, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.get_user_by_id(user_id)

@user_router.post("/create", response_model=UserCreate, status_code=status.HTTP_200_OK)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    service = UserService(db)
    return await service.create_user(user)

