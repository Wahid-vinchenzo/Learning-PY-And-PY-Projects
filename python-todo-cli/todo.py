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
# todo.py (mark_complete changes)

tasks_file = "tasks.txt"  # lines: title||0 or title||1

def save_tasks():
    with open(tasks_file, "w", encoding="utf-8") as f:
        for t in tasks:
            # t is tuple (title, done_bool)
            f.write(f"{t[0]}||{1 if t[1] else 0}\n")

def load_tasks():
    try:
        with open(tasks_file, "r", encoding="utf-8") as f:
            out = []
            for line in f:
                line = line.rstrip("\n")
                if "||" in line:
                    title, done = line.rsplit("||", 1)
                    out.append((title, bool(int(done))))
                elif line:
                    # backward compatibility (old plain title)
                    out.append((line, False))
            return out
    except FileNotFoundError:
        return []

# initialize
tasks = load_tasks()

def show_tasks():
    if not tasks:
        print("No tasks.")
    else:
        for i, (title, done) in enumerate(tasks, 1):
            status = "✓" if done else " "
            print(f"{i}. [{status}] {title}")

def add_task(task):
    tasks.append((task, False))
    save_tasks()
    print(f"Task '{task}' added.")

def delete_task(index):
    try:
        removed = tasks.pop(index-1)
        save_tasks()
        print(f"Task '{removed}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")
        print(f"Task '{removed[0]}' deleted.")
    except (IndexError, ValueError):
        print("Invalid task number.")

def mark_task_done(index):
    try:
        title, _ = tasks[index-1]
        tasks[index-1] = (title, True)
        save_tasks()
        print(f"Task '{title}' marked completed.")
    except (IndexError, ValueError):
        print("Invalid task number.")
print("Goodbye from A!")
