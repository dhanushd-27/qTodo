import click
from core.db import delete_todo

@click.command()
@click.argument("todo_id", type=int)
def rm(todo_id: int):
    """Remove a task."""
    if delete_todo(todo_id):
        click.echo(f"Task {todo_id} deleted.")
    else:
        click.echo(f"Error: Task {todo_id} not found.")
