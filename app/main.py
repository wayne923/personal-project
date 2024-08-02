from fastapi import FastAPI

from app.routers import decks

app = FastAPI()

app.include_router(decks.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}