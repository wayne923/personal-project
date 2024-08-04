from sqlalchemy import String, Integer, Column, text, TIMESTAMP, ForeignKey, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column

from app.config.database import Base


class Card(Base):
    __tablename__ = "card"

    id = Column(Integer, primary_key=True, nullable=False)
    deck_id: Mapped[int] = mapped_column(ForeignKey("deck.id"))
    front = Column(String, nullable=False)
    back = Column(String, nullable=False)
    creation_date = Column(DateTime(timezone=True), server_default=func.now())



