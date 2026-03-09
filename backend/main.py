from fastapi import FastAPI

from database import get_db
from app.routes. users_route import user_router

app = FastAPI()

app.include_router(user_router)

@app.get("/info")
async def info():
    return {"message": "info"}