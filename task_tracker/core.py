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

def remove_task(id: int) -> bool:
    tasks = load_db()
    for task in tasks:
        if task['id'] == id:
            tasks.remove(task)
            save_tasks(tasks)
            return True
    return False

def mark_as_concluded(task_id: int) -> bool:
    tasks = load_db()
    for task in tasks:
        if task['id'] == task_id:
            if task['done']:
                return 'already done'
            
            task['done'] = True
            save_tasks(tasks)
            return 'done'
    return 'not found'