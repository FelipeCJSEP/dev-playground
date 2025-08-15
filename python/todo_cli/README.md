[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/) 
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen)](https://github.com/your-username/todo_cli/actions)
[![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

# To-Do List CLI Application

A simple **Command-Line Interface (CLI) To-Do List** application in Python, allowing users to manage tasks with features such as adding, editing, completing, cancelling, and removing tasks. Tasks are stored in a JSON file for persistence.

---

## Features

- Add new tasks with title, description, responsible person, and priority.
- List all tasks with detailed information.
- Search tasks by ID.
- Mark tasks as completed or cancelled.
- Edit tasks that are in progress.
- Remove tasks.
- Persistent storage using JSON.
- Fully tested with unit tests, including input simulation.

---

## Installation

1. Clone the repository:

```bash
git clone <your-repo-url>
cd todo_cli
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

Dependencies:
- tabulate (for displaying tables in CLI)

---

## Usage

Run the main program:
```bash
python main.py
```

You will see a menu like this:
```bash
To-Do List Menu:
1. Add Task
2. List Tasks
3. Search Task by ID
4. Complete Task
5. Cancel Task
6. Edit Task
7. Remove Task
8. Exit
```

## Project Structure

```bash
todo_cli/
│
├── todo/                  # Main package
│   ├── __init__.py
│   ├── cli.py             # CLI interface
│   ├── task_manager.py    # Task management logic
│   ├── task.py            # Task dataclass and enums
│   └── storage.py         # JSON storage handling
│
├── tests/                 # Unit tests
│   ├── __init__.py
│   ├── test_task_manager_with_mocked_input.py
|   └── test_task_manager.py
│
├── data/                  # JSON file storage
│   └── tasks.json
│
├── main.py                # Entry point of the application
└── README.md
```

---

## Running Tests

The project includes automated tests using unittest with input simulation (mock).

Run all tests:
```bash
python -m unittest discover -s tests -v
```

Expected output:
........
----------------------------------------------------------------------
Ran 14 tests in 0.035s

OK

## License

This project is licensed under the MIT License.
