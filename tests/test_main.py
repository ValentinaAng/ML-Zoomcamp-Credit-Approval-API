import json
from pathlib import Path

import pytest
from fastapi import status
from fastapi.testclient import TestClient

from app.main import app


# Define test client
@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


# Load test data from file
file_path = Path("tests/data/test_data.json")

with file_path.open("r") as f:
    test_data = json.load(f)


def test_main(client: TestClient) -> None:
    response = client.post("/predict", json=test_data)
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"prediction": 0, "status": "Credit Loan Denied"}
