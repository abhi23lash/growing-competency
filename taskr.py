import json
import sys
from pathlib import Path

DB = Path(__file__).with_name("tasks.json")


def load():
    if DB.exists():
        return json.loads(DB.read_text())
    return []


def save(tasks):
    DB.write_text(json.dumps(tasks, indent=2))


def add(title):
    tasks = load()
    tasks.append({"title": title, "done": False})
    save(tasks)
    print(f"Added: {title}")


def done(number):
    tasks = load()
    tasks[number - 1]["done"] = True
    save(tasks)
    print(f"Completed: {tasks[number - 1]['title']}")
def delete(number):
    tasks = load()
    removed = tasks.pop(number - 1)
    save(tasks)
    print(f"Deleted: {removed['title']}")


def list_tasks():
    tasks = load()
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        mark = "x" if t["done"] else " "
        print(f"{i}. [{mark}] {t['title']}")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["list"]
    if cmd == "add":
        add(" ".join(args))
    elif cmd == "done":
        done(int(args[0]))
    elif cmd == "delete":
        delete(int(args[0]))
    else:
        list_tasks()
