from src.database.connection import init_db, engine
from src.database.security import setup_row_level_security
from sqlmodel import Session

if __name__ == "__main__":
    print("Initializing database...")
    init_db()

    # Set up Row Level Security
    print("Setting up Row Level Security...")
    with Session(engine) as db:
        setup_row_level_security(db)

    print("Database initialized successfully!")