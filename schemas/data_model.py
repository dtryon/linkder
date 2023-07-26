from pydantic import BaseModel


class Card(BaseModel):
    Distance_from_London: int = Field(None, ge=0, le=100)
    Past_employers: int = Field(None, ge=0, le=100)
    Qualifications: int = Field(None, ge=0, le=100)
    Emojis_in_profile: int = Field(None, ge=0, le=100)
