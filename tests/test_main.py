from fastapi import status
from fastapi.testclient import TestClient
import pytest
from app.main import app
import json


# Define test client
@pytest.fixture
def client():
    return TestClient(app)


# Load test data from file
with open("./data/test_data.json") as f:
    test_data = json.load(f)


def test_main(client: TestClient) -> None:
    response = client.post("/predict", json=test_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"prediction": 0, "status": "Credit Loan Denied"}
