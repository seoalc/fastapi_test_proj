from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_wallet_info_endpoint():
    wallet_address = "TXYZ1234567890abcdefghijklmnopqrstuvw"

    response = client.post("/api/wallet-info/", json={"wallet_address": wallet_address})

    assert response.status_code == 200
    data = response.json()
    assert "wallet_address" in data
    assert "balance" in data
    assert "bandwidth" in data
    assert "energy" in data

    response = client.get("/api/wallet-requests/")
    assert response.status_code == 200
    requests = response.json()
    assert len(requests) > 0
    assert requests[0]["wallet_address"] == wallet_address