from app.config.database import Base, engine

from app.models.card import Card
from app.models.deck import Deck


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Deck.metadata.create_all(bind=engine)
    Card.metadata.create_all(bind=engine)