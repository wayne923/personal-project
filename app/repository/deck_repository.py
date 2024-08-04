from sqlalchemy.orm import Session
from typing import List, Optional, Type
from pydantic import UUID4

from app.models.deck import Deck
from app.schemas.deck_schema import Deck as DeckIO


class DeckRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: DeckIO) -> Deck:
        deck = Deck(**data.model_dump(exclude_none=True))
        self.session.add(deck)
        self.session.commit()
        self.session.refresh(deck)
        return DeckIO(title=deck.title, cards=deck.cards)

    def get_all(self) -> List[Optional[DeckIO]]:
        pass
    def get_deck(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass