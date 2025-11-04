# todo.py (update)
tasks_file = "tasks.txt"

def save_tasks():
    try:
        with open(tasks_file, "w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t + "\n")
    except Exception as e:
        print("Error saving tasks:", e)

def load_tasks():
    try:
        with open(tasks_file, "r", encoding="utf-8") as f:
            return [line.rstrip("\n") for line in f]
    except FileNotFoundError:
        return []
    except Exception as e:
        print("Error loading tasks:", e)
        return []

# replace tasks = [] with:
tasks = load_tasks()
# and after add_task and delete_task, call save_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added.")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        save_tasks()
        print(f"Task '{removed}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")
