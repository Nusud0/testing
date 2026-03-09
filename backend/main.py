from fastapi import FastAPI

from database import get_db

app = FastAPI()




@app.get("/info")
async def info():
    return {"message": "info"}