from aiogoogle import Aiogoogle
from fastapi import APIRouter, Depends
from pydantic import HttpUrl
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.core.google_client import get_service
from app.core.user import current_superuser
from app.crud.charity_project import charity_project_crud
from app.services.google_api import (
    set_user_permissions, spreadsheets_create, spreadsheets_update_value
)


DOCS_URL = 'https://docs.google.com/spreadsheets/d/{spreadsheet_id}'


router = APIRouter()


@router.get(
    '/',
    response_model=str,
    dependencies=[Depends(current_superuser)],
)
async def get_report(
        session: AsyncSession = Depends(get_async_session),
        wrapper_services: Aiogoogle = Depends(get_service)

):
    projects = await charity_project_crud.get_sorted_closed_projects(session)
    spreadsheet_id, spreadsheet_url = await spreadsheets_create(
        wrapper_services
    )
    await set_user_permissions(spreadsheet_id, wrapper_services)
    try:
        await spreadsheets_update_value(
            spreadsheet_id, projects, wrapper_services
        )
    except ValueError as error:
        return str(error)
    return spreadsheet_url
