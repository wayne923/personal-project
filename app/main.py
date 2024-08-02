from fastapi import FastAPI

from app.router.v1 import deck

app = FastAPI()

app.include_router(deck.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}