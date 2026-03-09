from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from database import get_db
from ..models.user_model import User
from ..schemas.user_schemas import UserCreate, UserGet


async def get_all_users(db: AsyncSession):
    result = await db.execute(select(User))

    users = result.scalars().all()

    if not users:
        raise

    return users


async def create_user(user: UserCreate, db: AsyncSession):
    new_user = User(**user.model_dump()) 
        
    db.add(new_user)  # БЕЗ await!
        
    try:
        await db.commit()      # Сохраняем (с await)
        await db.refresh(new_user) # Обновляем объект, чтобы получить ID из БД
    except Exception as e:
        await db.rollback()    # Если ошибка (например, email занят), откатываем
        raise HTTPException(status_code=400, detail=str(e))
            
    return new_user
