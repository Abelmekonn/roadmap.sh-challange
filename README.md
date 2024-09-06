# Task Tracker CLI

A simple command-line interface (CLI) application to track and manage tasks. This CLI allows you to add, update, delete, and list tasks, as well as mark tasks as in progress or done.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as in progress or done
- List all tasks or filter tasks by status (todo, in-progress, done)
- Create a JSON file to store tasks if it does not exist

## Requirements

- Python 3.x

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli
   ```

2. **Ensure Python is Installed**

   Make sure Python 3.x is installed on your system. You can check this with:

   ```bash
   python --version
   ```

## Usage

Run the CLI commands using the following syntax:

### Add a New Task

```bash
python cli.py add "Task description"
```

**Example:**

```bash
python cli.py add "Buy groceries"
```

*Output:* `Task added successfully (ID: 1)`

### Update an Existing Task

```bash
python cli.py update TASK_ID "New task description"
```

**Example:**

```bash
python cli.py update 1 "Buy groceries and cook dinner"
```

*Output:* `Task 1 updated successfully.`

### Delete a Task

```bash
python cli.py delete TASK_ID
```

**Example:**

```bash
python cli.py delete 1
```

*Output:* `Task 1 deleted successfully.`

### Mark a Task as In Progress

```bash
python cli.py mark-in-progress TASK_ID
```

**Example:**

```bash
python cli.py mark-in-progress 1
```

*Output:* `Task 1 marked as in-progress.`

### Mark a Task as Done

```bash
python cli.py mark-done TASK_ID
```

**Example:**

```bash
python cli.py mark-done 1
```

*Output:* `Task 1 marked as done.`

### List All Tasks

```bash
python cli.py list
```

### List Tasks by Status

```bash
python cli.py list STATUS
```

**Valid Statuses:** `todo`, `in-progress`, `done`

**Example:**

```bash
python cli.py list done
```

### Create Tasks File

If the tasks file does not exist, you can create it with:

```bash
python cli.py create-file
```

*Output:* `Tasks file created.`

## Project Structure

- `cli.py`: The main CLI script to handle user commands.
- `src/`
  - `tasks.py`: Contains functions for task management (add, update, delete, mark, list).
- `data/`
  - `tasks.json`: JSON file where tasks are stored.

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
