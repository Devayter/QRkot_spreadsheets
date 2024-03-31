from datetime import datetime
from copy import deepcopy

from aiogoogle import Aiogoogle
from app.core.config import settings


ROW_COUNT = 100
COLUMN_COUNT = 11

FORMAT = "%Y/%m/%d %H:%M:%S"
SPREADSHEET_BODY = dict(
    properties=dict(
        title='Отчет от {now_date_time}',
        locale='ru_RU',
    ),
    sheets=[dict(properties=dict(
        sheetType='GRID',
        title='Лист1',
        gridProperties=dict(
            rowCount=ROW_COUNT,
            columnCount=COLUMN_COUNT,
        )
    ))]
)
TABLES_HEADER = [
    ['Отчёт от, {now_date_time}'],
    ['Топ проектов по скорости закрытия'],
    ['Название проекта', 'Время сбора', 'Описание']
]

MAX_ROWS_LIMIT_ERROR = (
    f'Количество строк превышает {ROW_COUNT}, невозможно создать документ'
)


async def spreadsheets_create(wrapper_services: Aiogoogle) -> str:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    spreadsheet_body = deepcopy(SPREADSHEET_BODY)
    spreadsheet_body['properties']['title'] = (
        spreadsheet_body['properties']['title'].format(
            now_date_time=now_date_time
        )
    )
    response = await wrapper_services.as_service_account(
        service.spreadsheets.create(json=spreadsheet_body)
    )
    return response['spreadsheetId'], response['spreadsheetUrl']


async def set_user_permissions(
        spreadsheet_id: str,
        wrapper_services: Aiogoogle
) -> None:
    permissions_body = {
        'type': 'user',
        'role': 'writer',
        'emailAddress': settings.email
    }
    service = await wrapper_services.discover('drive', 'v3')
    await wrapper_services.as_service_account(
        service.permissions.create(
            fileId=spreadsheet_id,
            json=permissions_body,
            fields="id"
        )
    )


async def spreadsheets_update_value(
        spreadsheet_id: str,
        projects: list,
        wrapper_services: Aiogoogle
) -> None:
    now_date_time = datetime.now().strftime(FORMAT)
    service = await wrapper_services.discover('sheets', 'v4')
    tables_header = deepcopy(TABLES_HEADER)
    tables_header[0][0] = (
        tables_header[0][0].format(now_date_time=now_date_time)
    )
    table_values = [
        *tables_header,
        *[
            list(map(
                str,
                [
                    project.name,
                    project.close_date - project.create_date,
                    project.description
                ]
            )) for project in projects
        ]
    ]
    if len(table_values) > ROW_COUNT:
        raise ValueError(MAX_ROWS_LIMIT_ERROR)
    update_body = {
        'majorDimension': 'ROWS',
        'values': table_values
    }
    await wrapper_services.as_service_account(
        service.spreadsheets.values.update(
            spreadsheetId=spreadsheet_id,
            range='R1C1:R100C11',
            valueInputOption='USER_ENTERED',
            json=update_body
        )
    )
