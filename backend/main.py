from fastapi import FastAPI

app = FastAPI()


@app.get("/info")
async def info():
    return {"message": "info"}