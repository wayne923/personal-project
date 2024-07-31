from fastapi import APIRouter

router = APIRouter()


@router.get("/decks/", tags=["decks"])
async def read_decks():
    return [{"deck_name": "Algo"}, {"deck_name": "Python"}]