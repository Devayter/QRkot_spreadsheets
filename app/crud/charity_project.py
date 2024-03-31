from sqlalchemy import desc, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models.charity_project import CharityProject


class CRUDCharityProject(CRUDBase):

    async def get_sorted_closed_projects(self, session: AsyncSession) -> list:
        return (
            await session.execute(
                select(
                    CharityProject
                ).where(CharityProject.fully_invested).order_by(
                    desc(
                        CharityProject.close_date - CharityProject.create_date
                    )
                )
            )
        ).scalars().all()


charity_project_crud = CRUDCharityProject(CharityProject)
