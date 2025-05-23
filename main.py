import typer
import json
from pathlib import Path


app = typer.Typer()
DATA_FILE = Path("tasks.json")

def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []
def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


@app.command()
def add(task: str):
    tasks = load_tasks()
    if task in tasks:
        print("Task has already been added, pick another name")
    else:
        print(f"Added {task} to list")
        tasks.append(task)
        save_tasks(tasks)
@app.command()
def remove(task: str):
    tasks = load_tasks()
    if task in tasks:
        print(f"Removed {task} from list")
        tasks.remove(task)
        save_tasks(tasks)
@app.command()
def list():
    tasks = load_tasks()
    if tasks:
        print("Tasks:")
        for tid, task in enumerate(tasks, start=1):
            print(f"{tid}. {task}")
    else:
        print("No tasks found")


if __name__ == '__main__':
    app()