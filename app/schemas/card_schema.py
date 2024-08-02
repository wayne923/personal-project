from pydantic import BaseModel


class Card(BaseModel):
    front: str
    back: str
