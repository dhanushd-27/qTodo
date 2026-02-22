import click
from core.db import create_todo
from models.todo import Todo
from utils import parse_date
from .utils import resolve_list

@click.command()
@click.argument("task", type=str)
@click.argument("list_identifier", type=str, required=False)
@click.option("--priority", "-p", type=int, default=2, help="Priority (1-3, default 2)")
@click.option("--duration", type=int, default=60, help="Duration in minutes (default 60)")
@click.option("--due", "-d", type=str, help="Due date (e.g., 'today', 'tomorrow', 'YYYY-MM-DD')")
def add(task: str, list_identifier: str, priority: int, duration: int, due: str):
    """Add a new task. Optionally append @listname."""
    if list_identifier is None and " @" in task:
        parts = task.split(" @")
        task = parts[0]
        list_identifier = parts[-1].split()[0]
    
    list_id, resolved_name = resolve_list(list_identifier)
    
    parsed_due_date = parse_date(due) if due else None
    if due and not parsed_due_date:
        click.echo(f"Error: Invalid due date format '{due}'.")
        return

    new_todo = Todo(task=task, priority=priority, duration=duration, due_date=parsed_due_date)
    create_todo(list_id, new_todo)
    click.echo(f"Added '{task}' to '{resolved_name}'.")
