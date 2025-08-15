"""Task Manager Module for the to-do list application."""
import textwrap
from datetime import datetime
from tabulate import tabulate
from todo.task import Task, TaskPriority, TaskStatus
from todo.storage import Storage

class TaskManager:
    """Class to manage tasks in the to-do list application."""

    def __init__(self):
        """Initializes the task manager with an empty task list."""
        self.tasks = Storage.load_tasks()
        self.next_id = 1 if not self.tasks else max(task.id for task in self.tasks) + 1

    def _has_tasks(self) -> bool:
        """Checks if there are any tasks in the task list."""

        if not self.tasks:
            print("No tasks available.")
            return False

        return True

    def _find_task_by_id(self, task_id) -> Task | None:
        """Finds a task by its ID."""
        try:
            task_id = int(task_id)
        except ValueError:
            return None

        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def _close_task(self, status: TaskStatus):
        """Closes a task with the given status."""
        if not self._has_tasks():
            return
        
        task_id = input(f"Enter the ID of the task to mark as {status.value.lower()}: ")
        task = self._find_task_by_id(task_id)

        if task.status != TaskStatus.IN_PROGRESS:
            print(f"Task '{task.title}' (ID: {task.id}) cannot be marked as {status.value.lower()}.")
            print("Only tasks that are 'In Progress' can be closed.")
            return

        if task:
            now = datetime.now()
            task.status = status
            task.updated_at = now
            task.closed_at = now
            Storage.save_tasks(self.tasks)
            print(f"Task '{task.title}' marked as {status.value.lower()}.")
        else:
            print(f"No task found with ID {task_id}.")

    def add_task(self):
        """Adds a new task to the task list."""
        print("Adding a new task...")
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        responsible = input("Enter responsible person: ")

        while True:
            priority_input = input("Enter task priority (Low, Medium, High): ").strip().upper()

            if priority_input in TaskPriority.__members__:
                priority = TaskPriority[priority_input]
                break

            print("Invalid priority. Please enter Low, Medium, or High.")

        task = Task(
            id=self.next_id,
            title=title,
            description=description,
            responsible=responsible,
            status=TaskStatus.IN_PROGRESS,
            priority=priority,
        )

        self.tasks.append(task)
        self.next_id += 1
        Storage.save_tasks(self.tasks)
        print(f"Task '{title}' added successfully. ID: {task.id}")

    def list_tasks(self):
        """Lists all tasks in the task list."""
        if not self._has_tasks():
            return

        table = []
        headers = ["ID", "Title", "Description", "Responsible", "Status", "Priority", "Created At", "Updated At", "Closed At"]

        for task in self.tasks:
            table.append([
                task.id,
                textwrap.fill(task.title, 20),
                textwrap.fill(task.description, 40),
                textwrap.fill(task.responsible, 20),
                task.status.value,
                task.priority.value,
                task.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                task.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                task.closed_at.strftime("%Y-%m-%d %H:%M:%S") if task.closed_at else "N/A"
            ])

        print(tabulate(table, headers=headers, tablefmt="grid"))

    def search_task_by_id(self):
        """Searches for a task by its ID."""
        if not self._has_tasks():
            return
        
        task_id = input("Enter the ID of the task to search: ")
        task = self._find_task_by_id(task_id)

        if task:
            print(f"\nTask Found (ID: {task.id}):")
            print(f"Title: {task.title}")
            print(f"Description: {task.description}")
            print(f"Responsible: {task.responsible}")
            print(f"Status: {task.status.value}")
            print(f"Priority: {task.priority.value}")
            print(f"Created At: {task.created_at}")
            print(f"Updated At: {task.updated_at}")

            if task.closed_at:
                print(f"Closed At: {task.closed_at}")
        else:
            print(f"No task found with ID {task_id}.")

    def complete_task(self):
        """Marks a task as completed."""
        self._close_task(TaskStatus.COMPLETED)

    def cancel_task(self):
        """Cancels a task."""
        self._close_task(TaskStatus.CANCELLED)

    def edit_task(self):
        """Edits an existing task."""
        if not self._has_tasks():
            return

        task_id = input("Enter the ID of the task to edit: ")
        task = self._find_task_by_id(task_id)

        if task.status != TaskStatus.IN_PROGRESS:
            print(f"Task '{task.title}' (ID: {task.id}) is not editable.")
            print("Only tasks that are 'In Progress' can be edited.")
            return

        if task:
            print(f"Editing Task '{task.title}' (ID: {task.id})")
            print(f"Description: {task.description}\n")
            new_title = input(f"Enter new title (leave blank to keep '{task.title}'): ")
            new_description = input("Enter new description (leave blank to keep current): ")
            new_responsible = input(f"Enter new responsible person (leave blank to keep '{task.responsible}'): ")

            while True:
                priority_input = input(f"Enter new priority (Low, Medium, High) or leave blank to keep '{task.priority.value}': ").strip().upper()

                if not priority_input:
                    break

                if priority_input in TaskPriority.__members__:
                    task.priority = TaskPriority[priority_input]
                    break

                print("Invalid priority. Please enter Low, Medium, or High.")

            if new_title.strip() != "":
                task.title = new_title

            if new_description.strip() != "":
                task.description = new_description

            if new_responsible.strip() != "":
                task.responsible = new_responsible

            task.updated_at = datetime.now()
            Storage.save_tasks(self.tasks)
            print(f"Task '{task.title}' updated successfully.")
        else:
            print(f"No task found with ID {task_id}.")

    def remove_task(self):
        """Removes a task from the task list."""
        if not self._has_tasks():
            return

        task_id = input("Enter the ID of the task to remove: ")
        task = self._find_task_by_id(task_id)

        if task:
            print(f"Removing Task '{task.title}' (ID: {task.id})")
            print("Do you want to proceed? (y/n): ")
            confirm = input().strip().lower()

            if confirm == 'y':
                self.tasks.remove(task)
                Storage.save_tasks(self.tasks)
                print(f"Task '{task.title}' removed successfully.")
            else:
                print("Task removal cancelled.")
        else:
            print(f"No task found with ID {task_id}.")
    