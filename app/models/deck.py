from typing import List

from sqlalchemy import String, Integer, Column, func, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.config.database import Base
from app.models.card import Card


class Deck(Base):
    __tablename__ = "deck"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())
