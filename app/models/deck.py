from sqlalchemy import String, Integer, Column, text, TIMESTAMP

from app.config.database import Base


class Deck(Base):
    __tablename__ = "decks"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)

