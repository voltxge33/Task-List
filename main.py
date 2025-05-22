import typer

app = typer.Typer(no_args_is_help=True)

@app.command()
def add(task: str):
    """

    Add a new task to the list
    """
    print(f"Added {task} to list")
@app.command()
def remove(task: str):
    """

    Remove a existing task from the list
    """
    print(f"Removed {task} from list")

if __name__ == "__main__":
    app()
