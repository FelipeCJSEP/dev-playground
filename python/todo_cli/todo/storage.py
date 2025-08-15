"""Storage Module for the to-do list application."""
import json
import os
from todo.task import Task

FILENAME = "data/tasks.json"

class Storage:
    """Handles the storage and retrieval of tasks."""

    @classmethod
    def load_tasks(cls):
        """Loads tasks from a JSON file."""
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)
                    return [Task.from_dict(task) for task in data]
                except json.JSONDecodeError:
                    return []
        return []

    @classmethod
    def save_tasks(cls, tasks: list[Task]):
        """Saves tasks to a JSON file."""
        with open(FILENAME, "w", encoding="utf-8") as file:
            # raise TypeError(f'Object of type {o.__class__.__name__} is not JSON serializable')
            json.dump([task.to_dict() for task in tasks], file, ensure_ascii=False, indent=4)
