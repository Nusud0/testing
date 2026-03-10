from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from ..models.user_model import User
from ..schemas.user_schemas import UserCreate, UserResponse


class UserRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_all(self) -> list[User]:
        result = await self.db.execute(select(User))

        users = result.scalars().all()

        if not users:
            raise

        return users

    async def get_by_id(self, user_id: int) -> User:
        result = await self.db.execute(select(User).where(User.id == user_id))

        user = result.scalar_one_or_none()

        return user


    async def create(self, user_data: UserCreate) -> User:
        new_user = User(**user_data.model_dump()) 
            
        self.db.add(new_user)  # БЕЗ await!
            
        try:
            await self.db.commit()      # Сохраняем (с await)
            await self.db.refresh(new_user) # Обновляем объект, чтобы получить ID из БД
        except Exception as e:
            await self.db.rollback()    # Если ошибка (например, email занят), откатываем
            raise HTTPException(status_code=400, detail=str(e))
                
        return new_user
