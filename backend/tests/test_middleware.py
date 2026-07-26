import pytest

@pytest.mark.asyncio
async def test_request_id_header(client):
    
    response = await client.get("/")
    
    assert response.status_code == 200
    
    assert "X-Request-ID" in response.headers