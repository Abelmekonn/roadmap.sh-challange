import argparse
from src.task_tracker import add_task, update_task, delete_task, mark_task, list_tasks, create_tasks_file


def main():
    parser = argparse.ArgumentParser(description='Task Tracker CLI')

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Add subparser
    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Task description')

    # Update subparser
    update_parser = subparsers.add_parser(
        'update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='Task ID')
    update_parser.add_argument(
        'description', type=str, help='New task description')

    # Delete subparser
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    # Mark-in-progress subparser
    mark_in_progress_parser = subparsers.add_parser(
        'mark-in-progress', help='Mark a task as in progress')
    mark_in_progress_parser.add_argument('id', type=int, help='Task ID')

    # Mark-done subparser
    mark_done_parser = subparsers.add_parser(
        'mark-done', help='Mark a task as done')
    mark_done_parser.add_argument('id', type=int, help='Task ID')

    # List subparser
    list_parser = subparsers.add_parser('list', help='List tasks')
    list_parser.add_argument('status', choices=[
                             'todo', 'in-progress', 'done'], nargs='?', help='Filter tasks by status')

    # Create-file subparser
    create_file_parser = subparsers.add_parser(
        'create-file', help='Create tasks file if it does not exist')

    args = parser.parse_args()

    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.id, args.description)
    elif args.command == 'delete':
        delete_task(args.id)
    elif args.command == 'mark-in-progress':
        mark_task(args.id, 'in-progress')
    elif args.command == 'mark-done':
        mark_task(args.id, 'done')
    elif args.command == 'list':
        list_tasks(args.status)
    elif args.command == 'create-file':
        create_tasks_file()


if __name__ == '__main__':
    main()
