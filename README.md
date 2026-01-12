# Todo App - Full Stack Web Application

## Project Structure

This repository contains a full-stack todo application with the following structure:

- `frontend/` - Next.js 16+ application with responsive UI
- `backend/` - FastAPI application with JWT authentication
- `specs/` - Specification files for both Phase I (CLI) and Phase II (Web)
- `todo-cli-app/` - Original Phase I CLI application
- `history/` - Development history and artifacts

## Phases

### Phase I: CLI Todo App (`todo-cli-app/`)
- Command-line interface only
- In-memory storage
- Single-user, single-session
- Basic CRUD operations

### Phase II: Full-Stack Web App (`frontend/` + `backend/`)
- Web-based interface with authentication
- Persistent storage in Neon PostgreSQL
- Multi-user support with data isolation
- JWT-based security
- Responsive design

For more details about the evolution from Phase I to Phase II, see [RELATIONSHIP.md](RELATIONSHIP.md).

## Setup

### Backend
```bash
cd backend
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -e .
uvicorn src.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Architecture

- **Frontend**: Next.js 16+ with App Router
- **Backend**: FastAPI with SQLModel ORM
- **Database**: Neon Serverless PostgreSQL
- **Authentication**: Better Auth with JWT
- **Spec System**: Spec-Kit Plus