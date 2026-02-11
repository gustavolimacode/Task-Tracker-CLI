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
