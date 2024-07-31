from typing import List

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Card(BaseModel):
    front: str
    back: str

class Deck(BaseModel):
    name: str
    Cards: List[Card]


@router.get("/decks/", tags=["decks"])
async def read_decks():
    return [{"deck_name": "Algo"}, {"deck_name": "Python"}]


@router.post("/deck/")
def create_deck():
    return {"message": "deck created"}


# need to define objects and models based on mock data for deck



