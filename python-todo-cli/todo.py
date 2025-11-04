# todo.py
tasks = []

def show_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        print(f"Task '{removed}' deleted.")
    except IndexError:
        print("Invalid task number.")

while True:
    print("\n1. View Tasks  2. Add Task  3. Delete Task  4. Exit")
    choice = input("Choose an option: ")
    
    if choice == "1":
        show_tasks()
    elif choice == "2":
        task = input("Enter task: ")
        add_task(task)
    elif choice == "3":
        index = int(input("Enter task number to delete: "))
        delete_task(index)
    elif choice == "4":
        break
    else:
        print("Invalid choice")
