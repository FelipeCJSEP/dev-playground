"""Command-line interface for the To-Do List application."""
import os
from todo.task_manager import TaskManager

task_manager = TaskManager()

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    """Displays the main menu options."""
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Search Task by ID")
    print("4. Complete Task")
    print("5. Cancel Task")
    print("6. Edit Task")
    print("7. Remove Task")
    print("8. Exit")

    try:
        option = int(input("Select an option (1-8): "))
    except ValueError:
        return False
    finally:
        clear_screen()

    if 1 <= option <= 7:
        if option == 1:
            task_manager.add_task()
        elif option == 2:
            task_manager.list_tasks()
        elif option == 3:
            task_manager.search_task_by_id()
        elif option == 4:
            task_manager.complete_task()
        elif option == 5:
            task_manager.cancel_task()
        elif option == 6:
            task_manager.edit_task()
        elif option == 7:
            task_manager.remove_task()

        input("\nPress Enter to continue...")
        clear_screen()

    return option == 8
