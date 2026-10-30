"Tests that run without starting a server."
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)
ORDER = {"distance_km": 5.0, "prep_time_min": 20, "traffic_level": 2, "rain": 0}


def test_health():
    assert client.get("/health").status_code == 200


def test_known_order():
    assert client.post("/predict", json=ORDER).json()["delivery_min"] == 43.0


def test_rain_is_slower():
    dry = client.post("/predict", json=ORDER).json()["delivery_min"]
    wet = client.post("/predict", json={**ORDER, "rain": 1}).json()["delivery_min"]
    assert wet > dry


def test_bad_traffic_is_rejected():
    assert client.post("/predict", json={**ORDER, "traffic_level": 9}).status_code == 422
