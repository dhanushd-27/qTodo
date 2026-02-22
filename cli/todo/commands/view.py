import click
from core.db import get_all_todos, todo_list_table, Q
from tabulate import tabulate
from utils import format_date

@click.command()
@click.argument("list_name", type=str)
def view(list_name: str):
    """View todos in a list."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    todos = get_all_todos(lst['id'])
    if not todos:
        click.echo(f"No todos found in '{list_name}'.")
        return
        
    table = [[t.id, "✓" if t.completed else " ", t.task, t.priority, f"{t.duration}m", format_date(t.created_at)] for t in todos]
    headers = ["ID", "Done", "Task", "Priority", "Duration", "Created At"]
    click.echo(f"\nTodos in '{list_name}':")
    click.echo(tabulate(table, headers=headers, tablefmt="grid"))