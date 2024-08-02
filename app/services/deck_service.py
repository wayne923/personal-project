from typing import List
from fastapi import HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session

from app.repository.deck_repository import DeckRepository


class DeckService:
    """
    Service class for handling decks.
    """

    def __init__(self, session: Session):
        self.repository = DeckRepository(session)

    def create(self):
        pass
    def delete(self):
        pass
    def get_all(self):
        pass
    def update(self):
        pass
