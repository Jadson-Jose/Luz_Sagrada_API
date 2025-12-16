from typing import List, Optional

from pydantic import BaseModel

from app.models.verse import Verse


class Chapter(BaseModel):
    number: int
    title: Optional[str] = None
    verses: List[Verse]
