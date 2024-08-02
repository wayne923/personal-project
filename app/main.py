from fastapi import FastAPI

from app.router import deck

app = FastAPI()

app.include_router(deck.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}