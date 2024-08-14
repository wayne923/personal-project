from typing import List
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.repository.deck_repository import DeckRepository
from app.schemas.deck_schema import Deck


class DeckService:
    """
    Service class for handling decks.
    """

    def __init__(self, session: Session):
        self.repository = DeckRepository(session)

    def create(self, data):
        if self.repository.region_exists_by_name(data.name):
            raise HTTPException(status_code=400, detail="Region already exists")
        return self.repository.create(data)
    def get_all(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass


