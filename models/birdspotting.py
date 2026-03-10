from datetime import datetime
from typing import Optional
from sqlmodel import Field, Relationship, SQLModel

from models.birds import Bird

class BirdspottingBase(SQLModel):
    bird_id: int = Field(foreign_key="birds.id")
    spotted_at: datetime = Field(default_factory=datetime.now)
    location: str
    observer_name: str
    notes: Optional[str] = None

class Birdspotting(BirdspottingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    # Allows you to access the bird object directly from a spotting
    bird: Optional["Bird"] = Relationship()

class BirdspottingCreate(BirdspottingBase):
    pass