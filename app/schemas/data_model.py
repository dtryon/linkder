from pydantic import BaseModel, Field


class Card(BaseModel):
    distance_from_london: int = Field(None, ge=0, le=100)
    past_employers: int = Field(None, ge=0, le=100)
    qualifications: int = Field(None, ge=0, le=100)
    emojis_in_profile: int = Field(None, ge=0, le=100)
