from fastapi import APIRouter

from app.router.v1 import deck, card

router = APIRouter(
    prefix="/api/v1"
)

router.include_router(deck.router)
router.include_router(card.router)
