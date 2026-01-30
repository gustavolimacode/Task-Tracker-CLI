import json
import os

DB_tasks = r"db/tasks_example.json"

def load_db():
    if not os.path.exists(DB_tasks):
        return []
    with open(DB_tasks, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(DB_tasks, 'w') as file:
        json.dump(tasks, file, indent=2)

def list_tasks():
    return load_db()

def add_task(title: str):
    tasks = load_db()
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'done': False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    return new_task