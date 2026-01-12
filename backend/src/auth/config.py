from better_auth import better_auth
from better_auth import SQLModelAdapter
from sqlmodel import create_engine
from ..config import settings

# Create database engine
engine = create_engine(settings.DATABASE_URL)

# Initialize Better Auth with SQLModel adapter
auth = better_auth(
    database=SQLModelAdapter(engine),
    secret=settings.JWT_SECRET_KEY,
    base_url="/api/auth",
    email_password={
        "enabled": True,
    },
    session_config={
        "session_ttl": settings.ACCESS_TOKEN_EXPIRE_MINUTES * 60,  # Convert to seconds
        "remember_me": False,
    }
)