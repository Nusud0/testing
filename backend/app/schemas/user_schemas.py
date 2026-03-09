from pydantic import BaseModel, Field

class UserGet(BaseModel):
    id: int = Field(..., description="User ID")
    name: str = Field(..., description="User name")

class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50, description="User name")
    