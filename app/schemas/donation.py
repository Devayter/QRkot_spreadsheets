from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field

from app.schemas.base import CharityProjectDonationBase
from app.schemas.schemas_examples import DONATION_SCHEMA_EXAMPLE


class DonationBase(CharityProjectDonationBase):
    comment: Optional[str] = Field(None, max_length=200)


class DonationCreate(DonationBase):
    full_amount: int = Field(gt=0)

    class Config:
        orm_mode = True
        json_schema_extra = DONATION_SCHEMA_EXAMPLE


class DonationDB(BaseModel):
    id: int
    full_amount: int
    comment: Optional[str]
    create_date: datetime

    class Config:
        orm_mode = True


class DonationSuperUserDB(DonationBase):
    id: int
    user_id: int