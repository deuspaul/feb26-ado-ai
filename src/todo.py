#!/usr/bin/env python3
"""
A simple command-line to-do list application using argparse and JSON storage.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path


class TodoApp:
    """A simple to-do list application with JSON persistence."""

    def __init__(self, tasks_file: str = "tasks.json"):
        """Initialize the TodoApp with a tasks file."""
        self.tasks_file = tasks_file
        self.tasks = self._load_tasks()

    def _load_tasks(self) -> list:
        """Load tasks from JSON file."""
        if os.path.exists(self.tasks_file):
            try:
                with open(self.tasks_file, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []

    def _save_tasks(self) -> None:
        """Save tasks to JSON file."""
        with open(self.tasks_file, "w") as f:
            json.dump(self.tasks, f, indent=2)

    def add_task(self, title: str, description: str = "") -> None:
        """Add a new task to the list."""
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "description": description,
            "completed": False,
            "created_at": datetime.now().isoformat(),
        }
        self.tasks.append(task)
        self._save_tasks()
        print(f"✓ Task added: {title}")

    def list_tasks(self, show_completed: bool = True) -> None:
        """List all tasks."""
        if not self.tasks:
            print("No tasks found.")
            return

        print("\n" + "=" * 60)
        print("TO-DO LIST".center(60))
        print("=" * 60)

        for task in self.tasks:
            if not show_completed and task["completed"]:
                continue

            status = "✓" if task["completed"] else "○"
            print(f"\n[{task['id']}] {status} {task['title']}")
            if task["description"]:
                print(f"    {task['description']}")
            print(f"    Created: {task['created_at']}")

        print("\n" + "=" * 60)

    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                self._save_tasks()
                print(f"✓ Task {task_id} marked as completed: {task['title']}")
                return
        print(f"✗ Task {task_id} not found.")

    def delete_task(self, task_id: int) -> None:
        """Delete a task by ID."""
        original_length = len(self.tasks)
        self.tasks = [task for task in self.tasks if task["id"] != task_id]
        if len(self.tasks) < original_length:
            self._save_tasks()
            print(f"✓ Task {task_id} deleted.")
        else:
            print(f"✗ Task {task_id} not found.")


def main():
    """Main entry point for the CLI application."""
    parser = argparse.ArgumentParser(
        description="A simple command-line to-do list application",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python todo.py add "Buy groceries" --desc "Milk, eggs, bread"
  python todo.py list
  python todo.py complete 1
  python todo.py delete 1
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Add command
    add_parser = subparsers.add_parser("add", help="Add a new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument(
        "--desc", "--description", dest="description", default="", help="Task description"
    )

    # List command
    list_parser = subparsers.add_parser("list", help="List all tasks")
    list_parser.add_argument(
        "--all",
        action="store_true",
        help="Show completed tasks (default: show only active tasks)",
    )

    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark a task as completed")
    complete_parser.add_argument("task_id", type=int, help="Task ID")

    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete a task")
    delete_parser.add_argument("task_id", type=int, help="Task ID")

    args = parser.parse_args()

    # Initialize the app
    app = TodoApp()

    # Execute commands
    if args.command == "add":
        app.add_task(args.title, args.description)
    elif args.command == "list":
        app.list_tasks(show_completed=args.all)
    elif args.command == "complete":
        app.complete_task(args.task_id)
    elif args.command == "delete":
        app.delete_task(args.task_id)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
