from typing import List

from fastapi import APIRouter


router = APIRouter()



@router.get("/cards/", tags=["cards"])
async def read_decks():
    return [{"card_name": "quicksort"}, {"card_name": "do something"}]


@router.post("/card/")
def create_deck():
    return {"message": "card created"}

