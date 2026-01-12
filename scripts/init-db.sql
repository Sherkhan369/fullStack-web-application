-- Initialize database schema for Todo Web Application
-- This script will be executed when the PostgreSQL container starts

-- Create extensions if they don't exist
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Verify database creation
SELECT 'Database initialization complete' as status;