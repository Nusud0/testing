from pydantic import BaseModel, Field, ConfigDict

class UserResponse(BaseModel):
    id: int = Field(..., description="User ID")
    name: str = Field(..., description="User name")

    class Config:
        form_attributes = True

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="User name")

class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int = Field(..., description="Total number of users")
