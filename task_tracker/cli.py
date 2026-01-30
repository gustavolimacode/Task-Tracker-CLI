import argparse
from core import add_task, list_tasks

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    parser.add_argument("command", choices=['add', 'list'], help="Task command to execute: add, list")
    parser.add_argument("--title", help="Task title (Required for the 'add' command).")

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


if __name__ == '__main__':
    main()