# feb26-ado-ai

A Python project featuring a command-line to-do list application with JSON-based task storage.

## Overview

This repository contains a simple yet functional CLI to-do list app built with Python. It demonstrates best practices for command-line argument parsing, file I/O, and data persistence using JSON.

## Project Structure

```
.
├── README.md          # This file
├── requirements.txt   # Python dependencies (minimal - uses built-in modules)
├── tasks.json         # JSON file storing all tasks
└── src/
    └── todo.py        # Main CLI application
```

## Features

- **Add Tasks**: Create new tasks with optional descriptions
- **List Tasks**: View all tasks with completion status
- **Complete Tasks**: Mark tasks as completed
- **Delete Tasks**: Remove tasks from your list
- **JSON Persistence**: Tasks are automatically saved and loaded from `tasks.json`
- **Clean CLI Interface**: Built with argparse for intuitive command-line usage

## Requirements

- Python 3.7 or higher
- No external dependencies required (uses only built-in modules)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/deuspaul/feb26-ado-ai.git
cd feb26-ado-ai
```

2. (Optional) Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Usage

Run the application with Python:

```bash
python3 src/todo.py --help
```

### Commands

#### Add a task
```bash
python3 src/todo.py add "Buy groceries"
python3 src/todo.py add "Buy groceries" --desc "Milk, eggs, bread"
```

#### List all tasks
```bash
python3 src/todo.py list
```

#### List all tasks including completed ones
```bash
python3 src/todo.py list --all
```

#### Mark a task as completed
```bash
python3 src/todo.py complete 1
```

#### Delete a task
```bash
python3 src/todo.py delete 1
```

## Data Storage

Tasks are stored in `tasks.json` in the following format:

```json
[
  {
    "id": 1,
    "title": "Task title",
    "description": "Optional description",
    "completed": false,
    "created_at": "2026-02-09T10:30:00.123456"
  }
]
```

## Architecture

The application uses a simple object-oriented design with a `TodoApp` class that handles:
- Task persistence (loading and saving)
- Task management operations (add, list, complete, delete)
- File I/O with proper error handling

The CLI interface is built using Python's standard `argparse` module for robust command parsing.

## Contributing

Contributions are welcome! Please create a branch from main for any new features or improvements.

## License

This project is open source and available under the MIT License.