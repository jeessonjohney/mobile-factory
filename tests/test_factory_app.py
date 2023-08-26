from starlette.testclient import TestClient
import os, sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from factory_app.app import app

client = TestClient(app)


def test_valid_order_request():
    data = {"components": ["A", "D", "F", "I", "K"]}
    response = client.post("/orders", json=data)
    print(response)
    assert response.status_code == 200
    result = response.json()["data"]
    assert "order_id" in result
    assert "total" in result
    assert "parts" in result


def test_invalid_order_request():
    data = {"components": ["A", "A", "D", "I", "K"]}
    response = client.post("/orders", json=data)
    assert response.status_code == 400
    assert "error" in response.json()["data"]

    data = {"components": ["A", "B", "D", "I"]}
    response = client.post("/orders", json=data)
    assert response.status_code == 400
    assert "error" in response.json()["data"]


def test_missing_components_field():
    data = {"wrong_field": ["A", "D", "F", "I", "K"]}
    response = client.post("/orders", json=data)
    assert response.status_code == 400


def test_invalid_component_id():
    data = {"components": ["A", "XYZ", "D", "I", "K"]}
    response = client.post("/orders", json=data)
    assert response.status_code == 400
    assert "error" in response.json()["data"]


def test_invalid_json():
    response = client.post("/orders", data="invalid-json")
    assert response.status_code == 400
