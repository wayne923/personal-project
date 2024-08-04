from pydantic import BaseModel
from typing import List

from app.schemas.card_schema import Card


class Deck(BaseModel):
    title: str
    cards: List[Card]
