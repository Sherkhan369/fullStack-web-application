"""
Test configuration for contract tests
"""
import pytest
from fastapi.testclient import TestClient

from backend.src.main import app


@pytest.fixture
def api_client():
    """API client for contract testing"""
    client = TestClient(app)
    yield client


def test_api_health_check(api_client):
    """Basic health check to ensure API is running"""
    response = api_client.get("/health")
    assert response.status_code == 200
    assert "status" in response.json()