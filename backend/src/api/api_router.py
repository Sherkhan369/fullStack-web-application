from fastapi import APIRouter

from src.api.v1 import auth, tasks

api_router = APIRouter()

# Include version 1 API routes
api_router.include_router(auth.router, prefix="/auth", tags=["authentication"])
api_router.include_router(tasks.router, prefix="/tasks", tags=["tasks"])