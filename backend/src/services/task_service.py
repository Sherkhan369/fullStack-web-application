from typing import List, Optional
from sqlalchemy.orm import Session

from src.models.task import Task, TaskCreate, TaskUpdate
from src.models.user import User


class TaskService:
    """Service layer for task management operations."""

    def __init__(self, db: Session):
        self.db = db

    def get_user_tasks(self, user: User) -> List[Task]:
        """Get all tasks for a specific user."""
        return self.db.query(Task).filter(Task.user_id == user.id).all()

    def get_task_by_id(self, task_id: str, user: User) -> Optional[Task]:
        """Get a specific task by ID for a user."""
        return self.db.query(Task).filter(
            Task.id == task_id,
            Task.user_id == user.id
        ).first()

    def create_task(self, task_data: TaskCreate, user: User) -> Task:
        """Create a new task for a user."""
        task = Task(**task_data.dict(), user_id=user.id)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def update_task(self, task_id: str, task_data: TaskUpdate, user: User) -> Optional[Task]:
        """Update a specific task for a user."""
        task = self.get_task_by_id(task_id, user)
        if not task:
            return None

        update_data = task_data.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(task, field, value)

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: str, user: User) -> bool:
        """Delete a specific task for a user."""
        task = self.get_task_by_id(task_id, user)
        if not task:
            return False

        self.db.delete(task)
        self.db.commit()
        return True

    def toggle_task_completion(self, task_id: str, user: User) -> Optional[Task]:
        """Toggle the completion status of a task."""
        task = self.get_task_by_id(task_id, user)
        if not task:
            return None

        task.is_complete = not task.is_complete
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task_statistics(self, user: User) -> dict:
        """Get task statistics for a user."""
        total_tasks = self.db.query(Task).filter(Task.user_id == user.id).count()
        completed_tasks = self.db.query(Task).filter(
            Task.user_id == user.id,
            Task.is_complete == True
        ).count()
        pending_tasks = total_tasks - completed_tasks

        return {
            "total": total_tasks,
            "completed": completed_tasks,
            "pending": pending_tasks,
            "completion_rate": (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }