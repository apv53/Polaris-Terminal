from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine
from sqlalchemy.pool import NullPool

from app.core.config import settings

engine: AsyncEngine = create_async_engine(
    settings.database_url,
    echo = settings.database_echo,
    future = True,
    poolclass = NullPool
)