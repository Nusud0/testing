from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from ..repositories.user_repository import UserRepository
from ..schemas.user_schemas import UserCreate, UserResponse, UserListResponse, UserUpdatePassword

class UserService:
    def __init__(self, db: AsyncSession):
        self.user_repository = UserRepository(db)


    async def get_all_users(self) -> UserListResponse:
        users = await self.user_repository.get_all()
        users_response = [UserResponse.model_validate(user) for user in users]
        return UserListResponse(users=users_response, total=len(users_response))
    
    async def get_user_by_id(self, user_id: int) -> UserResponse:
        user = await self.user_repository.get_by_id(user_id)

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"User with id {user_id} not found"
            )
        return UserResponse.model_validate(user)
    
    async def create_user(self, user_data: UserCreate) -> UserResponse:
        user = await self.user_repository.create(user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User data {user_data.name} not validate"
            )
        return UserResponse.model_validate(user)

    async def update_user_password(self, user_id: int, user_data: UserUpdatePassword) -> UserResponse:
        user = await self.user_repository.update_password(user_id, user_data)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"User data {user.name} not validate"
            )
        return UserResponse.model_validate(user)