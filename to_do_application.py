# simple_todo.py
# Beginner-friendly task manager (CLI) with persistence (stores tasks in tasks.json)

import json
import os

DATA_FILE = "tasks.json"  # file where tasks are saved

def load_tasks():
    """Load tasks from DATA_FILE. If file doesn't exist, return empty list."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            # If file is corrupted, start fresh
            return []

def save_tasks(tasks):
    """Save tasks (a list of dicts) to DATA_FILE."""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=2)

def display_tasks(tasks):
    """Show tasks with their index and completion status."""
    if not tasks:
        print("\nYour to-do list is empty.\n")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✓" if task.get("completed") else " "  # checkmark for completed
        print(f"{i}. [{status}] {task.get('name')}")
    print()  # blank line

def add_task(tasks):
    """Prompt user for a task name and add it to the list."""
    name = input("Enter the task name: ").strip()
    if name:
        tasks.append({"name": name, "completed": False})
        save_tasks(tasks)
        print(f"Task added: {name}\n")
    else:
        print("No task entered. Nothing added.\n")

def mark_task_completed(tasks):
    """Show tasks and let user mark one as completed."""
    if not tasks:
        print("No tasks to mark as completed.\n")
        return
    display_tasks(tasks)
    try:
        choice = int(input("Enter the task number to mark as completed: "))
        if 1 <= choice <= len(tasks):
            tasks[choice - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Marked task {choice} as completed.\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def remove_task(tasks):
    """Show tasks and let user remove one."""
    if not tasks:
        print("No tasks to remove.\n")
        return
    display_tasks(tasks)
    try:
        choice = int(input("Enter the task number to remove: "))
        if 1 <= choice <= len(tasks):
            removed = tasks.pop(choice - 1)
            save_tasks(tasks)
            print(f"Removed task: {removed.get('name')}\n")
        else:
            print("Invalid task number.\n")
    except ValueError:
        print("Please enter a valid number.\n")

def main():
    print("Welcome to the Simple To-Do List!")
    tasks = load_tasks()

    menu = (
        "Choose an option:\n"
        "1 - Display To-Do List\n"
        "2 - Add a Task\n"
        "3 - Mark a Task as Completed\n"
        "4 - Remove a Task\n"
        "5 - Quit\n"
    )

    while True:
        print(menu)
        choice = input("Enter choice (1-5): ").strip()
        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task_completed(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Goodbye! Your tasks are saved to", DATA_FILE)
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.\n")

if _name_ == "_main_":
    main()