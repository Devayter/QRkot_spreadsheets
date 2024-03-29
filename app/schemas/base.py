from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


MIN_STRING_LENGTH = 1


class CharityProjectDonationBase(BaseModel):
    full_amount: Optional[int] = Field(None, gt=0)
    invested_amount: int = 0
    fully_invested: bool = False
    create_date: datetime = Field(default_factory=datetime.now)
    close_date: Optional[datetime] = None

    class Config:
        min_anystr_length = MIN_STRING_LENGTH
        orm_mode = True
