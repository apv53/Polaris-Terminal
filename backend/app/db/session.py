from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.db.engine import engine

AsyncSessionFactory = async_sessionmaker(
    bind = engine,
    class_ = AsyncSession, 
    autoflush = False,
    expire_on_commit = False
)