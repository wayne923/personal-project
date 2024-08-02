from sqlalchemy.orm import Session
from typing import List, Optional, Type
from pydantic import UUID4


class DeckRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self):
        pass
    def get_all(self):
        pass
    def get_deck(self):
        pass
    def update(self):
        pass
    def delete(self):
        pass