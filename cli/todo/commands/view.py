import click
from core.db import get_all_todos, todo_list_table, Q
from tabulate import tabulate
from utils import format_date, parse_date
from datetime import datetime, timezone

@click.command()
@click.argument("list_name", type=str)
@click.option("--today", is_flag=True, help="Show todos due today (and pending past ones)")
@click.option("--tomorrow", is_flag=True, help="Show todos due tomorrow")
@click.option("--date", type=str, help="Show todos due on a specific date (YYYY-MM-DD)")
@click.option("--before", type=str, help="Show todos due before a specific date")
@click.option("--after", type=str, help="Show todos due after a specific date")
def view(list_name: str, today: bool, tomorrow: bool, date: str, before: str, after: str):
    """View todos in a list with optional date filtering."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    todos = get_all_todos(lst['id'])
    if not todos:
        click.echo(f"No todos found in '{list_name}'.")
        return
        
    filtered_todos = []
    
    # Pre-parse dates for filters
    now = datetime.now(timezone.utc).replace(hour=0, minute=0, second=0, microsecond=0)
    filter_date = parse_date(date) if date else None
    filter_before = parse_date(before) if before else None
    filter_after = parse_date(after) if after else None

    for t in todos:
        keep = True
        t_due = t.due_date
        
        # We only apply date filters if the task has a due date, except for pending tasks on today
        if today:
            # If it's not completed, and its due date is today OR it's in the past (pending), keep it
            if t_due:
                if t.completed and t_due < now:
                    keep = False
                elif t_due > now:
                    keep = False
            else:
                keep = False  # Or keep = True if you want non-dated ones? Usually today = only dated ones. Let's say keep=False
        elif tomorrow:
            if not t_due or t_due != now + __import__('datetime').timedelta(days=1):
                keep = False
        elif filter_date:
            if not t_due or t_due != filter_date:
                keep = False
        elif filter_before:
            if not t_due or t_due >= filter_before:
                keep = False
        elif filter_after:
            if not t_due or t_due <= filter_after:
                keep = False
                
        if keep:
            filtered_todos.append(t)
            
    if not filtered_todos:
        click.echo(f"No todos match the applied filters in '{list_name}'.")
        return

    table = [[t.id, "✓" if t.completed else " ", t.task, t.priority, f"{t.duration}m", format_date(t.due_date), format_date(t.created_at)] for t in filtered_todos]
    headers = ["ID", "Done", "Task", "Priority", "Duration", "Due Date", "Created At"]
    click.echo(f"\nTodos in '{list_name}':")
    click.echo(tabulate(table, headers=headers, tablefmt="grid"))