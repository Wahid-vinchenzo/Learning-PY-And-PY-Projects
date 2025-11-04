# todo.py
"""
Simple To-Do CLI (initial version)
Commands:
  1 -> View tasks
  2 -> Add task
  3 -> Delete task
  4 -> Exit
"""
tasks = []

def show_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"Task '{removed}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def main():
    while True:
        print("\n1. View Tasks  2. Add Task  3. Delete Task  4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            show_tasks()
        elif choice == "2":
            task = input("Enter task: ").strip()
            if task:
                add_task(task)
        elif choice == "3":
            try:
                index = int(input("Enter task number to delete: ").strip())
                delete_task(index)
            except ValueError:
                print("Please enter a number.")
        elif choice == "4":
            print("Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
