import argparse
from core import add_task, list_tasks, remove_task

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    parser.add_argument("command", choices=['add', 'list', 'remove'], help="Task command to execute: add, list, remove")
    parser.add_argument("--title", help="Task title (Required for the 'add' command).")
    parser.add_argument("--id", type=int, help="Task id (Required for the 'remove' command).")

    args = parser.parse_args()

    if args.command == 'add':
        if not args.title:
            print("Error: You need to specify the task title with '--title'.")
            return
        task = add_task(args.title)
        print(f"Task successfully added: {task['id']} - {task['title']}")

    elif args.command == 'list':
        tasks = list_tasks()
        if not tasks:
            print("No tasks found")
            return
        for task in tasks:
            status = 'x' if task.get('done') else " "
            print(f"[{status}] {task['id']} - {task['title']}")

    elif args.command == 'remove':
        if args.id is None:
            print("Error: You need to specify the task id with '--id'.")
            return
        
        removed = remove_task(args.id)

        if removed:
            print(f'Task {args.id} removed successfully.')
        else:
            print(f'Task with id {args.id} not found.')


if __name__ == '__main__':
    main()