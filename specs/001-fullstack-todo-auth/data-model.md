# Data Model: Phase II - Full-Stack Todo Web Application

**Date**: 2026-01-07
**Feature**: 001-fullstack-todo-auth
**Phase**: Phase 1 - Design

## Core Entities

### User Entity

**Purpose**: Represents an authenticated user account with secure credentials and personal information.

**Fields**:
- `id` (UUID): Unique identifier for the user
- `email` (String, unique): User's email address for login
- `password_hash` (String): Securely hashed password (never stored in plain text)
- `created_at` (DateTime): Account creation timestamp
- `updated_at` (DateTime): Last update timestamp
- `is_active` (Boolean): Account status (default: true)

**Validation Rules**:
- Email must be valid email format and unique across system
- Password must meet minimum security requirements (8+ characters)
- User cannot be deleted - account can be deactivated instead

**Relationships**:
- One-to-many with Task (User can have multiple tasks)
- Tasks are cascaded for deletion when user is deleted

**State Transitions**:
- Active ↔ Inactive (for account suspension)
- No direct deletion - soft delete via is_active flag

### Task Entity

**Purpose**: Represents a todo item with title, description, completion status, and ownership.

**Fields**:
- `id` (UUID): Unique identifier for the task
- `title` (String): Task title (required, 1-200 characters)
- `description` (Text, optional): Detailed task description
- `is_complete` (Boolean): Completion status (default: false)
- `created_at` (DateTime): Task creation timestamp
- `updated_at` (DateTime): Last update timestamp
- `user_id` (UUID, foreign key): Owner of the task

**Validation Rules**:
- Title is required and must not be empty
- Title length must be between 1-200 characters
- Description can be empty or up to 2000 characters
- Task must belong to a valid user
- Completion status defaults to false

**Relationships**:
- Many-to-one with User (Task belongs to one user)
- User isolation enforced - users can only access their own tasks

**State Transitions**:
- Pending → Complete (when task is marked done)
- Complete → Pending (when task is marked incomplete)
- Created → Deleted (when task is removed)

## Database Schema

```sql
-- Users table
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true,
    CONSTRAINT email_format CHECK (email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
);

-- Tasks table
CREATE TABLE tasks (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    is_complete BOOLEAN DEFAULT false,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    user_id UUID NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    CONSTRAINT title_length CHECK (length(trim(title)) > 0 AND length(title) <= 200),
    CONSTRAINT description_length CHECK (description IS NULL OR length(description) <= 2000)
);

-- Indexes for performance
CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_is_complete ON tasks(is_complete);
CREATE INDEX idx_tasks_created_at ON tasks(created_at);

-- Row-Level Security policies
ALTER TABLE users ENABLE ROW LEVEL SECURITY;
ALTER TABLE tasks ENABLE ROW LEVEL SECURITY;

-- Users can only see their own data
CREATE POLICY user_isolation_policy ON users
    FOR ALL
    USING (true); -- Users can see their own account

CREATE POLICY task_user_isolation_policy ON tasks
    FOR ALL
    USING (user_id = current_setting('app.current_user_id')::UUID);
```

## Data Access Patterns

### User Operations
1. **Create User**: Insert new user with hashed password
2. **Find User by Email**: For authentication
3. **Update User**: Update profile information
4. **Deactivate User**: Set is_active to false

### Task Operations
1. **Create Task**: Insert new task with user ownership
2. **List User Tasks**: Retrieve all tasks for a specific user
3. **Get Task by ID**: Retrieve specific task with user validation
4. **Update Task**: Modify task details with ownership verification
5. **Delete Task**: Remove task with cascade deletion
6. **Toggle Completion**: Update is_complete status

### Security Considerations
- **User Isolation**: Row-Level Security ensures users can only access their own data
- **Password Security**: Use bcrypt or similar for password hashing
- **JWT Claims**: Include user_id in JWT tokens for API authorization
- **Input Validation**: Validate all user inputs to prevent injection attacks
- **Audit Trail**: Consider adding audit logs for sensitive operations

## Migration Strategy

### From Phase I (CLI) to Phase II (Web)
1. **Data Migration**: Export CLI data to compatible format
2. **User Creation**: Create user accounts for existing CLI users
3. **Task Migration**: Associate existing tasks with new user accounts
4. **Password Reset**: Require password setup for security

### Schema Evolution
- Start with basic schema as defined above
- Add audit fields (created_by, updated_by) if needed
- Consider soft delete patterns if hard delete is too destructive
- Add indexes based on query performance analysis

## Performance Considerations

### Query Optimization
- Index user_id on tasks table for fast user-specific queries
- Consider partial indexes for completed tasks if querying patterns require it
- Use connection pooling for database connections
- Implement query result caching for frequently accessed data

### Scalability
- UUID primary keys provide better distribution than auto-increment integers
- Consider sharding strategy if user base grows significantly
- Monitor query performance and add indexes as needed
- Use database connection pooling and query optimization

## Data Validation Rules

### User Validation
- Email format validation using regex
- Password strength requirements
- Uniqueness constraints on email
- Proper handling of null/empty values

### Task Validation
- Title length and content validation
- User ownership validation
- Date/time format validation
- Boolean state validation for completion status