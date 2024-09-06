
```markdown
# Task Tracker CLI

Sample solution for a Task Tracker CLI project. This project is a command-line interface (CLI) tool to track and manage tasks. 

## How to Run

Clone the repository and set up the project:

```bash
git clone [https://github.com/yourusername/task-tracker-cli](https://github.com/Abelmekonn/roadmap.sh-challange/blob/main/Task%20Tracker%20Cli).git
cd task-tracker-cli
```

Ensure Python 3.x is installed on your system. You can check this with:

```bash
python --version
```

Run the following command to use the CLI:

```bash
python cli.py --help # To see the list of available commands

# To add a task
python cli.py add "Buy groceries"

# To update a task
python cli.py update 1 "Buy groceries and cook dinner"

# To delete a task
python cli.py delete 1

# To mark a task as in-progress/done/todo
python cli.py mark-in-progress 1
python cli.py mark-done 1
python cli.py mark-todo 1

# To list all tasks
python cli.py list
python cli.py list done
python cli.py list todo
python cli.py list in-progress

# To create the tasks file if it does not exist
python cli.py create-file
```

## Project Structure

- `cli.py`: The main CLI script to handle user commands.
- `src/`
  - `tasks.py`: Contains functions for task management (add, update, delete, mark, list).
- `data/`
  - `tasks.json`: JSON file where tasks are stored.

## Usage

### Commands

- **Add a Task:**
  ```bash
  python cli.py add "Task description"
  ```
  Example: `python cli.py add "Buy groceries"`

- **Update a Task:**
  ```bash
  python cli.py update TASK_ID "New task description"
  ```
  Example: `python cli.py update 1 "Buy groceries and cook dinner"`

- **Delete a Task:**
  ```bash
  python cli.py delete TASK_ID
  ```
  Example: `python cli.py delete 1`

- **Mark a Task:**
  ```bash
  python cli.py mark-in-progress TASK_ID
  python cli.py mark-done TASK_ID
  python cli.py mark-todo TASK_ID
  ```
  Example: `python cli.py mark-done 1`

- **List Tasks:**
  ```bash
  python cli.py list
  python cli.py list STATUS
  ```
  Valid statuses: `todo`, `in-progress`, `done`

  Example: `python cli.py list done`

- **Create Tasks File:**
  ```bash
  python cli.py create-file
  ```

## Contributing

If you want to contribute to this project, please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Project URL

For more information, visit the project repository at: [https://github.com/yourusername/task-tracker-cli](https://github.com/yourusername/task-tracker-cli)
```
