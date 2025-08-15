"""Test with mocked input module for the to-do list application"""
import unittest
import os
from unittest.mock import patch
from todo.task import Task, TaskStatus, TaskPriority
from todo.task_manager import TaskManager
from todo.storage import Storage

class TestTaskManagerWithMockedInput(unittest.TestCase):
    """Test various functionalities of the TaskManager class with mocked input."""

    def setUp(self):
        """Set up environment before each test."""
        self.task_manager = TaskManager()
        self.task_manager.tasks = []
        self.task_manager.next_id = 1

        # Use a separate test file to avoid touching real data
        self.original_filename = Storage.FILENAME if hasattr(Storage, 'FILENAME') else None
        Storage.FILENAME = "tests/test_tasks.json"

        if os.path.exists(Storage.FILENAME):
            os.remove(Storage.FILENAME)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(Storage.FILENAME):
            os.remove(Storage.FILENAME)
        if self.original_filename:
            Storage.FILENAME = self.original_filename

    @patch("builtins.input", side_effect=["Test Task", "Description", "Felipe", "High"])
    def test_add_task_using_mocked_input(self, mock_input):
        """Test adding a task using mocked input."""
        self.task_manager.add_task()
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].title, "Test Task")
        self.assertEqual(self.task_manager.tasks[0].priority, TaskPriority.HIGH)
        self.assertEqual(self.task_manager.tasks[0].status, TaskStatus.IN_PROGRESS)

    @patch("builtins.input", side_effect=["1"])
    def test_complete_task_using_mocked_input(self, mock_input):
        """Test completing a task using mocked input."""
        task = Task(
            id=1,
            title="Task to Complete",
            description="Complete me",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.MEDIUM
        )
        self.task_manager.tasks.append(task)
        self.task_manager.complete_task()

        self.assertEqual(task.status, TaskStatus.COMPLETED)
        self.assertIsNotNone(task.closed_at)

    @patch("builtins.input", side_effect=["1"])
    def test_cancel_task_using_mocked_input(self, mock_input):
        """Test cancelling a task using mocked input."""
        task = Task(
            id=1,
            title="Task to Cancel",
            description="Cancel me",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.LOW
        )
        self.task_manager.tasks.append(task)
        self.task_manager.cancel_task()

        self.assertEqual(task.status, TaskStatus.CANCELLED)
        self.assertIsNotNone(task.closed_at)

    @patch("builtins.input", side_effect=["1", "New Title", "New Description", "Maria", "High"])
    def test_edit_task_using_mocked_input(self, mock_input):
        """Test editing a task using mocked input."""
        task = Task(
            id=1,
            title="Old Title",
            description="Old Description",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.MEDIUM
        )
        self.task_manager.tasks.append(task)
        self.task_manager.edit_task()

        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "New Description")
        self.assertEqual(task.responsible, "Maria")
        self.assertEqual(task.priority, TaskPriority.HIGH)

    @patch("builtins.input", side_effect=["1", "y"])
    def test_remove_task_using_mocked_input(self, mock_input):
        """Test removing a task using mocked input."""
        task = Task(
            id=1,
            title="Task to Remove",
            description="Remove me",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.LOW
        )
        self.task_manager.tasks.append(task)
        self.task_manager.remove_task()

        self.assertEqual(len(self.task_manager.tasks), 0)

if __name__ == "__main__":
    unittest.main()
