"""Dataclass and Enums for Task representation in a to-do list application."""
from dataclasses import dataclass
from typing import Optional
from enum import Enum
from datetime import datetime

class TaskStatus(Enum):
    """Enumeration for task status."""
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"

class TaskPriority(Enum):
    """Enumeration for task priority levels."""
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

@dataclass
class Task:
    """Dataclass to represent a task in the to-do list application."""
    id: int
    title: str
    description: str
    responsible: str
    status: TaskStatus
    priority: TaskPriority
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
    closed_at: Optional[datetime] = None

    def to_dict(self):
        """Converts the Task instance to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "responsible": self.responsible,
            "status": self.status.value,
            "priority": self.priority.value,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
            "closed_at": self.closed_at.isoformat() if self.closed_at else None
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Task instance from a dictionary."""
        return cls(
            id=data["id"],
            title=data["title"],
            description=data["description"],
            responsible=data["responsible"],
            status=TaskStatus(data["status"]),
            priority=TaskPriority(data["priority"]),
            created_at=datetime.fromisoformat(data["created_at"]),
            updated_at=datetime.fromisoformat(data["updated_at"]),
            closed_at=datetime.fromisoformat(data["closed_at"]) if data["closed_at"] else None
        )