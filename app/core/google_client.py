from aiogoogle import Aiogoogle # noqa
from aiogoogle.auth.creds import ServiceAccountCreds

from app.core.config import settings


SCOPES = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]
INFO = {
    'type': settings.type,
    'project_id': settings.project_id,
    'private_key_id': settings.private_key_id,
    'private_key': "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCZzN7C1OihokU5\nA3DJyJuCywpilKxqC2K2njc+HwN0RZ0vb1CRCaYV8uQHUuoZgvhlnFYKeKteVvA1\nTTo8bFXjR5O4m+FiAMomvJqW8tMNp9J2upfQIGshFCA49P4ybq6cftaA3ID9jRnS\nxttiLhNZ4OYI5k5RSjmt6V9Yl+ZjFLo/Pr/rJjMBxpsQNUWjxItjlRbG4EHfHCip\nifdVal+8iOe4CLTSV5driBZmuxgR0dd/EuzpOOrBS1Rctikqu6f0ay2bm1sT403M\nlXPaV/fkpm5ec3LGIqTfYYu1xZtIQOaUGg5dAm5YgQZYUhb7Xez5+f0cyAy9ZjO1\n7fOn6g+rAgMBAAECggEAPFbHaFmeQNeIX+NNKyUUeb5NvzpD4EDCRBITa0BAmyu6\njMMXsSc/bSoDMypg5IxhBoBMs0P/O35RNCAtwkngclABEPK6/DeCF6tz3Ne8XIWk\nSOdQqxsk3G/oamAXoFKTF5udbSXVR2RFps9Uf5LDDcZxiTlNrY+4zFWcDgZeIS2D\naC1tv5iQy9cpiNZwDY9KRvVqmL1xVK4yDLmMaz0jFqPXc1GNAbAi1CX9qJ260xYd\n0bCuQYz5L7ElEgF7UMme8NJFc1reEW4bOqzI0EUMigEb1Et9QnYXTMwyMAq4i9si\nK90moNK2/sxEAi2+cPliSO5wVPrTzxuuIi2/hpIGUQKBgQDG2PR+Dw3wFyQhzTa7\nTpNgYlYtJI3Z6MdbXJtsrpvgUkormsc6NV8oxHkMpE0iegLzE3uWzOu++DVHb35C\nLGv9a54OpmME3lWYLXHOXANVhQHY95L8rB3JqxcsRas8gP6XJwc+QUXmUs0HhE2s\nO995lOzD299/K+4UkEL29Oob2wKBgQDGAWBRIgq/D9AqeY/ZO/GPyI+KeNPFnjrO\n0JFGwSLqsKTmITLW51/8bV8uVYjxQjtC3u8MxIbF1ThQSq5HTR5bzs8oye93BLCL\nz5kZmiu0Vv59Gok+4zqmPG9huwSDuMAbaaKfJFIU8Dqhhm7B83bfBdbQIJKZd5Ew\nqEPp+4iMcQKBgQCEwhbCDvUERb723lbbSUO2BxF4BD68rOBky/hs4ErrwqUIZcb7\nwuRsiHg1C4EAMqvDdE+ASAJhNsADmJmYPqY+xNn69/WGK5bEChtAZkhHkYzBOdGl\n5pfgq9zFzyHbPFg9vG3mj5fGhaOjkB53jmXOe7JztVmLQ14p1oMO9EdVHwKBgDMh\nz9mjzNqiHsOZOMiEblEPHeJIaYey4MTfn2SCI54vl6XGFPbiMStiox24APEshVkz\ncM//QD5+XVh+sJrBE4Hp2h1SaIB3uY+hQIwYAAlGHdn4rFCNJWwgVzMJtJS/dPyf\nPtuR6ZB2qO1lZdy4Ho5hV6PPhYwUEG5cRY164zxBAoGAJNrVGGRQVkLKQcYT8bFF\nG2UDzl4UKxlaU4HP/UT65yMWQaV7YfYTaMtnBl+uFzsMXvh/lvHQE0TMIKDh7Ybf\nr/5L9r3OJBNT7sbWb+CBs0yycx5+oJjZKrUvLAeCrNpp15/NvGddFiImpJVl3DAp37QlwHHYuD7EmvVDBVw19PI=\n-----END PRIVATE KEY-----",
    'client_email': settings.client_email,
    'client_id': settings.client_id,
    'auth_uri': settings.auth_uri,
    'token_uri': settings.token_uri,
    'auth_provider_x509_cert_url': settings.auth_provider_x509_cert_url,
    'client_x509_cert_url': settings.client_x509_cert_url
}

cred = ServiceAccountCreds(scopes=SCOPES, **INFO)


async def get_service():
    async with Aiogoogle(service_account_creds=cred) as aiogoogle:
        yield aiogoogle
