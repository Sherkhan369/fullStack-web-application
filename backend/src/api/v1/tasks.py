from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from uuid import UUID

from src.auth import get_current_active_user
from src.database import get_session
from src.models.task import Task, TaskCreate, TaskRead, TaskUpdate
from src.models.user import User

router = APIRouter()


@router.get("/", response_model=list[TaskRead])
async def list_tasks(
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """List all tasks for the current user."""
    tasks = db.query(Task).filter(Task.user_id == current_user.id).all()
    return tasks


@router.post("/", response_model=TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """Create a new task for the current user."""
    task = Task(**task_data.dict(), user_id=current_user.id)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/{task_id}", response_model=TaskRead)
async def get_task(
    task_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """Get a specific task by ID."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    return task


@router.put("/{task_id}", response_model=TaskRead)
async def update_task(
    task_id: UUID,
    task_data: TaskUpdate,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """Update a specific task."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    update_data = task_data.dict(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """Delete a specific task."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()
    return None


@router.patch("/{task_id}/toggle", response_model=TaskRead)
async def toggle_task_completion(
    task_id: UUID,
    current_user: User = Depends(get_current_active_user),
    db: Session = Depends(get_session),
):
    """Toggle task completion status."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == current_user.id).first()

    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found",
        )

    task.is_complete = not task.is_complete
    db.add(task)
    db.commit()
    db.refresh(task)
    return task