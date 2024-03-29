from sqlalchemy import Column, String

from app.models.base import CharityDonation


CHARITYPROJECT_REPRESENTATION = (
    'Имя: {name}\n'
    'Описание: {description}\n'
)


class CharityProject(CharityDonation):
    name = Column(String)
    description = Column(String)

    def __repr__(self):
        return (
            super().__repr__() +
            CHARITYPROJECT_REPRESENTATION.format(
                name=self.name,
                description=self.description
            )
        )
