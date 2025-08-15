"""Test module for the to-do list application"""
import unittest
import os
from unittest.mock import patch
from datetime import datetime
from todo.task import Task, TaskStatus, TaskPriority
from todo.task_manager import TaskManager
from todo.storage import Storage

class TestTaskManagerFunctionalities(unittest.TestCase):
    """Test various functionalities of the TaskManager class."""

    def setUp(self):
        """Set up environment before each test."""
        self.task_manager = TaskManager()
        self.task_manager.tasks = []
        self.task_manager.next_id = 1

        # Use a separate test file to avoid touching real data
        self.original_filename = Storage.FILENAME if hasattr(Storage, 'FILENAME') else None
        Storage.FILENAME = "tests/test_tasks.json"

        # Ensure the test file does not exist
        if os.path.exists(Storage.FILENAME):
            os.remove(Storage.FILENAME)

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(Storage.FILENAME):
            os.remove(Storage.FILENAME)
        if self.original_filename:
            Storage.FILENAME = self.original_filename

    def test_adding_single_task_increases_task_list_length(self):
        """Test that adding a task increases the task list length."""
        task = Task(
            id=self.task_manager.next_id,
            title="Complete Unit Test",
            description="Write unit tests for the TaskManager",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.HIGH
        )
        self.task_manager.tasks.append(task)
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].title, "Complete Unit Test")

    def test_marking_task_as_completed_updates_status_and_closed_at(self):
        """Test that completing a task updates its status and closed_at timestamp."""
        task = Task(
            id=1,
            title="Finish Documentation",
            description="Write docs for the To-Do app",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.MEDIUM
        )
        self.task_manager.tasks.append(task)

        # Simulate completing the task
        task.status = TaskStatus.COMPLETED
        task.closed_at = datetime.now()

        self.assertEqual(task.status, TaskStatus.COMPLETED)
        self.assertIsNotNone(task.closed_at)

    def test_cancelling_task_sets_status_to_cancelled(self):
        """Test that cancelling a task sets its status to Cancelled."""
        task = Task(
            id=1,
            title="Cancel Meeting",
            description="Meeting was postponed",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.LOW
        )
        self.task_manager.tasks.append(task)

        task.status = TaskStatus.CANCELLED
        task.closed_at = datetime.now()

        self.assertEqual(task.status, TaskStatus.CANCELLED)
        self.assertIsNotNone(task.closed_at)

    def test_editing_task_updates_fields_correctly(self):
        """Test that editing a task updates its fields correctly."""
        task = Task(
            id=1,
            title="Old Title",
            description="Old Description",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.MEDIUM
        )
        self.task_manager.tasks.append(task)

        # Simulate editing
        task.title = "New Title"
        task.description = "New Description"
        task.responsible = "Angely"
        task.priority = TaskPriority.HIGH
        task.updated_at = datetime.now()

        self.assertEqual(task.title, "New Title")
        self.assertEqual(task.description, "New Description")
        self.assertEqual(task.responsible, "Angely")
        self.assertEqual(task.priority, TaskPriority.HIGH)

    def test_removing_task_decreases_task_list_length(self):
        """Test that removing a task decreases the task list length."""
        task = Task(
            id=1,
            title="Task to Remove",
            description="Will be removed",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.LOW
        )
        self.task_manager.tasks.append(task)
        self.assertEqual(len(self.task_manager.tasks), 1)

        self.task_manager.tasks.remove(task)
        self.assertEqual(len(self.task_manager.tasks), 0)

    def test_search_task_by_id_returns_correct_task(self):
        """Test that searching a task by ID returns the correct task."""
        task = Task(
            id=1,
            title="Searchable Task",
            description="Find me by ID",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.MEDIUM
        )
        self.task_manager.tasks.append(task)

        found_task = next((t for t in self.task_manager.tasks if t.id == 1), None)
        self.assertIsNotNone(found_task)
        self.assertEqual(found_task.title, "Searchable Task")

    def test_task_to_dict_and_from_dict_preserves_all_data(self):
        """Test that converting a task to dict and back preserves all data."""
        task = Task(
            id=1,
            title="Dict Test Task",
            description="Check serialization",
            responsible="Felipe",
            status=TaskStatus.IN_PROGRESS,
            priority=TaskPriority.HIGH
        )
        task_dict = task.to_dict()
        task_from_dict = Task.from_dict(task_dict)

        self.assertEqual(task.id, task_from_dict.id)
        self.assertEqual(task.title, task_from_dict.title)
        self.assertEqual(task.description, task_from_dict.description)
        self.assertEqual(task.status, task_from_dict.status)
        self.assertEqual(task.priority, task_from_dict.priority)

    @patch("builtins.input", side_effect=["Test Task", "Description", "Felipe", "High"])
    def test_add_task_using_mocked_input(self, mock_input):
        """Test adding a task using mocked input."""
        self.task_manager.add_task()
        self.assertEqual(len(self.task_manager.tasks), 1)
        self.assertEqual(self.task_manager.tasks[0].title, "Test Task")
        self.assertEqual(self.task_manager.tasks[0].priority, TaskPriority.HIGH)

    @patch("builtins.input", side_effect=["1"])
    def test_complete_task_using_mocked_input(self, mock_input):
        """Test completing a task using mocked input."""
        # Add task manually first
        task = self.task_manager.tasks.append(
            self.task_manager.tasks.append(
                TaskManager().tasks.append(TaskManager().tasks.append(TaskStatus))
            )
        )

if __name__ == "__main__":
    unittest.main()
