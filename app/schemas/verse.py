from pydantic import BaseModel


class Verse(BaseModel):
    number: int
    text: str
