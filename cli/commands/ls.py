import click
from datetime import datetime, timezone
from core.db import get_all_todos
from utils import parse_date, format_date
from tabulate import tabulate
from .utils import resolve_list

@click.command()
@click.argument("list_identifier", type=str, required=False)
@click.option("--due", "-d", type=str, help="Filter by due date")
@click.option("--all", "show_all", is_flag=True, help="Show all (including past pending and future)")
def ls(list_identifier: str, due: str, show_all: bool):
    """List tasks in the current or specified list."""
    list_id, resolved_name = resolve_list(list_identifier)
    todos = get_all_todos(list_id)
    
    if not todos:
        click.echo(f"No tasks in '{resolved_name}'.")
        return

    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    filter_date = parse_date(due) if due else None
    
    filtered = []
    for t in todos:
        keep = True
        if not show_all:
            if due:
                if not t.due_date or t.due_date != filter_date:
                    keep = False
            else:
                if t.completed and t.due_date and t.due_date < now:
                    keep = False
        if keep:
            filtered.append(t)
            
    if not filtered:
        click.echo(f"No tasks match the filter in '{resolved_name}'.")
        return

    table = [[t.id, "✓" if t.completed else " ", t.task, t.priority, format_date(t.due_date)] for t in filtered]
    headers = ["ID", "Done", "Task", "Pri", "Due"]
    click.echo(f"\n{resolved_name}:")
    click.echo(tabulate(table, headers=headers, tablefmt="simple"))
