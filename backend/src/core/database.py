from libsql_experimental import create_client
from src.core.config import settings

client = create_client(
    url=settings.DATABASE_URL,
    auth_token=settings.DATABASE_AUTH_TOKEN.get_secret_value(),
)
