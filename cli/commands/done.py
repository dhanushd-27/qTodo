import click
from core.db import toggle_todo

@click.command()
@click.argument("todo_id", type=int)
def done(todo_id: int):
    """Toggle a task's completion status."""
    todo = toggle_todo(todo_id)
    if not todo:
        click.echo(f"Error: Task {todo_id} not found.")
        return
    status = "completed" if todo.completed else "uncompleted"
    click.echo(f"Task {todo_id} marked as {status}.")
