from sqlalchemy import String, Boolean, Integer, Column, text, TIMESTAMP
from .database import Base



class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)

