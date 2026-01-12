from typing import Generator

from sqlmodel import Session, create_engine, SQLModel

from src.config import settings

# Create database engine
engine = create_engine(
    settings.DATABASE_URL,
    echo=settings.DATABASE_ECHO,
    pool_pre_ping=True,
    pool_recycle=3600,
)

def get_session() -> Generator[Session, None, None]:
    """Get database session."""
    with Session(engine) as session:
        yield session

def init_db() -> None:
    """Initialize database tables."""
    from src.models import User, Task  # noqa: F401

    # Create tables
    SQLModel.metadata.create_all(engine)