# Quickstart Guide: Phase II - Full-Stack Todo Web Application

**Version**: 1.0.0
**Date**: 2026-01-07
**Feature**: 001-fullstack-todo-auth

## Prerequisites

### System Requirements
- **Node.js**: 18.17+ (for Next.js frontend)
- **Python**: 3.11+ (for FastAPI backend)
- **Docker**: Latest version (for local database setup)
- **Git**: For version control

### External Services
- **Neon PostgreSQL**: Account for production database
- **Environment Variables**: Required for authentication and database connections

## Setup Instructions

### 1. Environment Setup

#### Backend Setup
```bash
# Navigate to backend directory
cd backend/

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
uv pip install fastapi sqlmodel better-auth[fastapi] psycopg2-binary

# Install development dependencies
uv pip install pytest pytest-asyncio httpx
```

#### Frontend Setup
```bash
# Navigate to frontend directory
cd frontend/

# Install dependencies
npm install

# Install additional dependencies
npm install react-query @tanstack/react-query zod @hookform/resolvers
```

### 2. Database Configuration

#### Local Development (Docker)
```bash
# Start PostgreSQL database locally
docker-compose up -d

# Run database migrations
python backend/src/database/migrate.py
```

#### Production (Neon)
1. Create account at [Neon.tech](https://neon.tech)
2. Create a new project and database
3. Get connection string from Neon dashboard
4. Configure environment variables (see below)

### 3. Environment Variables

Create `.env` files for both backend and frontend:

#### Backend `.env`
```bash
# Database
DATABASE_URL="postgresql://user:password@localhost:5432/todoapp"

# Authentication
JWT_SECRET_KEY="your-super-secret-jwt-key-change-this-in-production"
JWT_ALGORITHM="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7

# Application
DEBUG=True
```

#### Frontend `.env.local`
```bash
NEXT_PUBLIC_API_BASE_URL="http://localhost:8000"
NEXT_PUBLIC_WS_URL="ws://localhost:8000"
```

**⚠️ Security Note**: Never commit `.env` files to version control. Use `.env.example` templates instead.

### 4. Running the Application

#### Start Backend
```bash
cd backend/
uv run python -m uvicorn src.main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Frontend
```bash
cd frontend/
npm run dev
```

### 5. Application URLs

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## Development Workflow

### Code Structure

```
backend/
├── src/
│   ├── models/           # SQLModel database models
│   ├── schemas/          # Pydantic validation schemas
│   ├── services/         # Business logic
│   ├── api/              # FastAPI route handlers
│   ├── auth/             # Authentication middleware
│   └── database/         # Database connection/session
└── tests/                # Backend tests

frontend/
├── src/
│   ├── app/              # Next.js App Router pages
│   ├── components/       # Reusable React components
│   ├── lib/              # Utilities and hooks
│   ├── services/         # API client services
│   └── styles/           # CSS-in-JS styling
└── tests/                # Frontend tests
```

### Running Tests

#### Backend Tests
```bash
cd backend/
uv run pytest tests/ -v
```

#### Frontend Tests
```bash
cd frontend/
npm test
```

#### E2E Tests
```bash
# Using Playwright
npx playwright test
```

### Database Operations

#### Migrations
```bash
# Run migrations
python backend/src/database/migrate.py

# Reset database (development only)
python backend/src/database/reset.py
```

#### Seed Data
```bash
# Add sample data
python backend/src/database/seed.py
```

## API Usage Examples

### Authentication

#### Register User
```bash
curl -X POST http://localhost:8000/api/v1/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "mypassword123"
  }'
```

#### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "password": "mypassword123"
  }'
```

### Task Management

#### Create Task
```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Complete project documentation",
    "description": "Write comprehensive documentation for the todo app"
  }'
```

#### Get Tasks
```bash
curl -X GET http://localhost:8000/api/v1/tasks \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"
```

#### Update Task
```bash
curl -X PUT http://localhost:8000/api/v1/tasks/TASK_ID \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "is_complete": true
  }'
```

## Common Development Tasks

### Adding New API Endpoints
1. Define Pydantic schemas in `backend/src/schemas/`
2. Create route handlers in `backend/src/api/`
3. Add database models in `backend/src/models/` if needed
4. Write tests in `backend/tests/`

### Adding New Frontend Components
1. Create component in `frontend/src/components/`
2. Add routing in `frontend/src/app/`
3. Implement API service in `frontend/src/services/`
4. Write tests in appropriate test directories

### Database Changes
1. Update models in `backend/src/models/`
2. Create migration script in `backend/src/database/migrations/`
3. Run migration with `python backend/src/database/migrate.py`

## Troubleshooting

### Common Issues

#### Port Already in Use
```bash
# Check what's using the port
lsof -i :8000
# Kill the process
kill -9 PID
```

#### Database Connection Issues
```bash
# Check if PostgreSQL is running
docker ps
# Restart database
docker-compose restart
```

#### CORS Issues
- Ensure frontend and backend are configured with correct origins
- Check environment variables for API base URLs

#### Authentication Issues
- Verify JWT secret key is consistent between services
- Check token expiration settings
- Ensure proper token storage and retrieval

### Getting Help

1. **Check Logs**: Both frontend and backend provide detailed error logs
2. **API Documentation**: Visit http://localhost:8000/docs for interactive API docs
3. **Issue Tracking**: Use the project's issue tracker for bugs and feature requests

## Next Steps

After completing setup:

1. **Explore the Codebase**: Familiarize yourself with the project structure
2. **Run the Tests**: Ensure all tests pass in both backend and frontend
3. **Start Development**: Begin implementing features according to the task list
4. **Follow Spec-Driven Development**: Ensure all changes align with approved specifications

## Production Deployment

For production deployment:

1. **Environment Variables**: Use proper secrets management
2. **Database**: Configure Neon PostgreSQL connection
3. **Authentication**: Use strong JWT secrets and proper token management
4. **SSL/TLS**: Enable HTTPS for all communications
5. **Monitoring**: Set up logging and monitoring services

See deployment documentation for detailed production setup instructions.