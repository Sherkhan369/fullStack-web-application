"""
Test configuration for integration tests
"""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.src.main import app
from backend.src.database import get_db
from backend.src.models import Base


@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the FastAPI app"""
    client = TestClient(app)
    yield client


@pytest.fixture
def mock_db_session():
    """Mock database session for testing"""
    # This would typically create an in-memory database for testing
    engine = create_engine("sqlite:///test.db", connect_args={"check_same_thread": False})
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base.metadata.create_all(bind=engine)

    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()