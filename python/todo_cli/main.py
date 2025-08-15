"""Main module to run the To-Do List application."""
from todo.cli import show_menu

def main():
    """Main function to run the To-Do List application."""
    while True:
        should_exit = show_menu()

        if should_exit:
            print("Exiting the To-Do List application. Goodbye!")
            break

if __name__ == "__main__":
    main()
