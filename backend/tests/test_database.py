from sqlalchemy import text

from app.db.session import async_session_factory

async def test_database_connection():
    
    async with async_session_factory() as session:
        result = await session.execute(text("SELECT 1"))
        
        assert result.scalar() == 1