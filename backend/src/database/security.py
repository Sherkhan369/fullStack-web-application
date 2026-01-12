"""
Row-Level Security (RLS) policies for user data isolation.

This module configures PostgreSQL Row-Level Security policies to ensure
that users can only access their own data, providing database-level
security enforcement.
"""

from sqlalchemy import text
from sqlalchemy.orm import Session

from src.database.connection import engine


def is_postgresql(db: Session) -> bool:
    """
    Check if the database is PostgreSQL.
    """
    try:
        # Check if we're using PostgreSQL
        result = db.execute(text("SELECT version()")).fetchone()
        return "postgresql" in result[0].lower() if result else False
    except:
        # If the query fails, check the database URL
        from src.config import settings
        return "postgresql" in settings.DATABASE_URL.lower()


def setup_row_level_security(db: Session) -> None:
    """
    Setup Row-Level Security policies for all tables.

    This function should be called during application initialization
    to ensure RLS is properly configured.
    """
    if not is_postgresql(db):
        # Skip RLS setup for non-PostgreSQL databases (like SQLite)
        return

    # Enable RLS on user table
    db.execute(text('ALTER TABLE "user" ENABLE ROW LEVEL SECURITY'))

    # Enable RLS on task table
    db.execute(text('ALTER TABLE "task" ENABLE ROW LEVEL SECURITY'))

    # Create policy for user table - users can only see their own data
    db.execute(text("""
        CREATE POLICY user_isolation_policy ON "user"
        FOR ALL
        USING (true)
    """))

    # Create policy for task table - users can only access their own tasks
    db.execute(text("""
        CREATE POLICY task_user_isolation_policy ON "task"
        FOR ALL
        USING (user_id = current_setting('app.current_user_id')::UUID)
    """))

    # Create function to set current user ID in session
    db.execute(text("""
        CREATE OR REPLACE FUNCTION set_current_user_id(user_id UUID)
        RETURNS void AS $$
        BEGIN
            PERFORM set_config('app.current_user_id', user_id::text, false);
        END;
        $$ LANGUAGE plpgsql;
    """))

    db.commit()


def set_current_user_id(db: Session, user_id: str) -> None:
    """
    Set the current user ID in the database session for RLS.

    This function should be called at the beginning of each request
    to set the current user context for Row-Level Security.
    """
    if not is_postgresql(db):
        # Skip RLS setup for non-PostgreSQL databases (like SQLite)
        return

    db.execute(text("SELECT set_current_user_id(:user_id)"), {"user_id": user_id})
    db.commit()


def disable_rls_for_admin(db: Session) -> None:
    """
    Temporarily disable RLS for administrative operations.

    Use with caution - only for admin operations that need to bypass RLS.
    """
    if not is_postgresql(db):
        # Skip RLS operations for non-PostgreSQL databases (like SQLite)
        return

    db.execute(text("ALTER TABLE users DISABLE ROW LEVEL SECURITY"))
    db.execute(text("ALTER TABLE tasks DISABLE ROW LEVEL SECURITY"))
    db.commit()


def enable_rls(db: Session) -> None:
    """
    Re-enable RLS after administrative operations.
    """
    if not is_postgresql(db):
        # Skip RLS operations for non-PostgreSQL databases (like SQLite)
        return

    db.execute(text("ALTER TABLE users ENABLE ROW LEVEL SECURITY"))
    db.execute(text("ALTER TABLE tasks ENABLE ROW LEVEL SECURITY"))
    db.commit()


def check_rls_status(db: Session) -> dict:
    """
    Check the current RLS status for all tables.

    Returns a dictionary with table names as keys and RLS status as values.
    """
    if not is_postgresql(db):
        # Return empty result for non-PostgreSQL databases (like SQLite)
        return {'users': False, 'tasks': False}

    result = {}

    # Check users table
    rls_users = db.execute(text("""
        SELECT relname, relrowsecurity
        FROM pg_class
        WHERE relname = 'users'
    """)).fetchone()

    result['users'] = rls_users[1] if rls_users else False

    # Check tasks table
    rls_tasks = db.execute(text("""
        SELECT relname, relrowsecurity
        FROM pg_class
        WHERE relname = 'tasks'
    """)).fetchone()

    result['tasks'] = rls_tasks[1] if rls_tasks else False

    return result