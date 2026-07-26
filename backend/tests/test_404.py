import pytest

@pytest.mark.asyncio
async def test_unkown_route(client):
    response = await client.get("/this-route-does-not-exist")
    
    assert response.status_code == 404