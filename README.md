# 📝 Task Tracker CLI

![CI](https://github.com/gustavolimacode/Task-Tracker-CLI/actions/workflows/ci.yml/badge.svg)

A minimal and clean Command Line Interface (CLI) application for managing tasks.  
Built with Python, fully tested with pytest, and integrated with GitHub Actions CI.

This project was created as a learning exercise to practice:
- Writing modular Python code
- Automated testing
- Continuous Integration (CI) pipelines

## Features

- Add new tasks
- List all tasks
- Remove tasks by ID
- Mark tasks as completed
- Store tasks in a lightweight JSON database
- Fully tested with 'pytest'
- Continuous Integration with GitHub Actions

## 📁 Project Structure

```task-tracker-cli/
├── task_tracker/
│   ├── init.py
│   ├── cli.py            # Command Line Interface (argparse)
│   └── core.py           # Business logic and task operations
├── tests/
│   └── test_core.py      # Unit tests for the core module
├── db/
│   └── tasks_example.json  # Local JSON database
├── .github/
│   └── workflows/
│       └── ci.yml        # GitHub Actions CI pipeline
├── .gitignore
└── README.md
```

## 🚀 Installation

Clone the repository:
```bash
git clone https://github.com/gustavolimacode/Task-Tracker-CLI.git
cd Task-Tracker-CLI
```

(Optional) Create and activate a virtual environment:
```
python -m venv .venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

Install development dependencies:
```
pip install pytest
```

## ▶️ Usage

You can run the CLI using Python's `-m` module syntax:
```bash
python -m task_tracker/cli.py <command> [options]
```
Add a new task
```
python -m task_tracker/cli.py add --title "Learn Python"
```
List all tasks
```
python -m task_tracker/cli.py list
```
Mark a task as completed
```
python -m task_tracker/cli.py done --id 1
```
Remove a task by ID
```
python -m task_tracker/cli.py remove --id 1
```

## 🧪 Running Tests

This project includes a full test suite for the core logic, written using `pytest`.

To run all tests, simply execute:
```bash
pytest -v
```
The tests cover:
- Adding tasks
- Listing tasks
- Removing tasks
- Marking tasks as completed
- Handling non-existent task IDs
- Handling tasks that are already completed

All tests run automatically in the GitHub Actions pipeline on every push or pull request.

## ⚙️ Continuous Integration (CI)

This project includes a GitHub Actions pipeline that runs automatically on every push and pull request.

The CI workflow performs:
- Checkout of the repository
- Python enviroment setup
- Installation of dependencies
- Execution of the full pytest test suite

If all tests pass, the pipeline is marked as successful.
If any test fails, the CI blocks the merge - ensuring code quality.

The workflow file is located at:
.github/workflows/ci.yml

You can also check the current CI status using the badge at the top of this README.
