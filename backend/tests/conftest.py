from httpx import AsyncClient, ASGITransport
from asgi_lifespan import LifespanManager
import pytest
import os

#SET ENVIRONMENT TO testing
os.environ["APP_ENVIRONMENT"] = "testing"

from app.main import app
from app.db.engine import engine

@pytest.fixture
async def client(): 
    async with LifespanManager(app):
        async with AsyncClient(
            transport = ASGITransport(app=app),
            base_url = "http://test") as client:
            yield client       

@pytest.fixture(scope = "session", autouse = True)
async def cleanup_engine():
    yield
    await engine.dispose()