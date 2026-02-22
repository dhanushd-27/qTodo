import click
from core.db import update_todo, get_todo, todo_list_table, Q
from datetime import datetime, timezone
from utils import parse_date

@click.command()
@click.argument("list_name", type=str)
@click.argument("todo_id", type=int)
@click.option("--task", "-t", type=str, help="New task description")
@click.option("--priority", "-p", type=int, help="New priority (1-3)")
@click.option("--duration", "-d", type=int, help="New duration in minutes")
@click.option("--due-date", type=str, help="New due date (e.g., 'today', 'tomorrow', 'YYYY-MM-DD')")
@click.option("--clear-due-date", is_flag=True, help="Remove the due date")
@click.option("--completed", "-c", type=bool, is_flag=True, help="Mark as completed")
@click.option("--uncompleted", "-u", type=bool, is_flag=True, help="Mark as uncompleted")
def update(list_name: str, todo_id: int, task: str, priority: int, duration: int, due_date: str, clear_due_date: bool, completed: bool, uncompleted: bool):
    """Update a todo item."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    todo = get_todo(todo_id)
    if not todo or todo.list_id != lst['id']:
        click.echo(f"Error: Todo with ID {todo_id} not found in list '{list_name}'.")
        return

    if not any([task, priority is None, duration is None, due_date, clear_due_date, completed, uncompleted]):
         click.echo("Error: Please provide at least one field to update.")
         return

    updates = {"updated_at": datetime.now(timezone.utc).isoformat()}
    if task: updates["task"] = task
    if priority is not None: updates["priority"] = priority
    if duration is not None: updates["duration"] = duration
    
    if due_date:
        parsed_due_date = parse_date(due_date)
        if not parsed_due_date:
            click.echo(f"Error: Invalid due date format '{due_date}'.")
            return
        updates["due_date"] = parsed_due_date.isoformat()
    elif clear_due_date:
        updates["due_date"] = None

    if completed: updates["completed"] = True
    elif uncompleted: updates["completed"] = False
    
    update_todo(todo_id, **updates)
    click.echo(f"Successfully updated todo {todo_id} in list '{list_name}'.")