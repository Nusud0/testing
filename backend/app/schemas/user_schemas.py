from pydantic import BaseModel, Field, ConfigDict

class UserResponse(BaseModel):
    id: int = Field(..., description="User ID")
    name: str = Field(..., description="User name")
    password: str = Field(..., description="User password")

    model_config = ConfigDict(from_attributes=True)

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="User name")
    password: str = Field(..., min_length=8, max_length=30, description="User password")

    model_config = ConfigDict(from_attributes=True)

class UserListResponse(BaseModel):
    users: list[UserResponse]
    total: int = Field(..., description="Total number of users")
 
class UserUpdatePassword(BaseModel):
    password: str