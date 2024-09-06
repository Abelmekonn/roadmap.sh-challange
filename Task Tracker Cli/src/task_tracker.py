import json
import os
from datetime import datetime

TASKS_FILE = 'data/tasks.json'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f, indent=4)
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(description):
    tasks = load_tasks()
    task_id = max([task['id'] for task in tasks], default=0) + 1
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': datetime.now().isoformat(),
        'updatedAt': datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = new_description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()
    original_length = len(tasks)
    tasks = [task for task in tasks if task['id'] != task_id]
    if len(tasks) < original_length:
        save_tasks(tasks)
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Task {task_id} not found.")

def mark_task(task_id, status):
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            if status in ['in-progress', 'done']:
                task['status'] = status
                task['updatedAt'] = datetime.now().isoformat()
                save_tasks(tasks)
                print(f"Task {task_id} marked as {status}.")
                return
            else:
                print("Invalid status. Use 'in-progress' or 'done'.")
                return
    print(f"Task {task_id} not found.")

def list_tasks(status=None):
    tasks = load_tasks()
    filtered_tasks = [task for task in tasks if status is None or task['status'] == status]
    for task in filtered_tasks:
        print(f"ID: {task['id']},\nDescription: {task['description']},\nStatus: {task['status']},\nCreatedAt: {task['createdAt']},\nUpdatedAt: {task['updatedAt']}")

def create_tasks_file():
    if not os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'w') as f:
            json.dump([], f, indent=4)
        print('Tasks file created.')
    else:
        print('Tasks file already exists.')
