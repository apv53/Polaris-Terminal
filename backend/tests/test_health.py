import pytest

@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/health")
    
    assert response.status_code == 200
    
    body = response.json()
    
    assert body["status"] == "healthy"
    assert "service" in body
    assert "version" in body
    assert "environment" in body
    
@pytest.mark.asyncio
async def test_live(client):
    response = await client.get("/live")
    
    assert response.status_code == 200
    assert response.json()["status"] == "alive"

@pytest.mark.asyncio
async def test_ready(client):
    response = await client.get("/ready")
    
    assert response.status_code == 200
    
    body = response.json()
    
    assert body["status"] == "ready"
    assert body["database"] == "connected"