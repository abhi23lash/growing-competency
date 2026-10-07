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


def list_tasks():
    tasks = load()
    if not tasks:
        print("No tasks yet.")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t['title']}")


if __name__ == "__main__":
    cmd, *args = sys.argv[1:] or ["list"]
    if cmd == "add":
        add(" ".join(args))
    else:
        list_tasks()
