import click
from core.db import create_todo, todo_list_table, Q
from models.todo import Todo

@click.command()
@click.argument("list_name", type=str)
@click.argument("task", type=str)
@click.option("--priority", "-p", type=int, default=2, help="Priority (1-3, default 2)")
@click.option("--duration", "-d", type=int, default=60, help="Duration in minutes (default 60)")
def add(list_name: str, task: str, priority: int, duration: int):
    """Add a new todo item."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    new_todo = Todo(task=task, priority=priority, duration=duration)
    create_todo(lst['id'], new_todo)
    click.echo(f"Successfully added todo '{task}' to list '{list_name}'.")
