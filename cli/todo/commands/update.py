import click
from core.db import update_todo, get_todo, todo_list_table, Q
from datetime import datetime, timezone

@click.command()
@click.argument("list_name", type=str)
@click.argument("id", type=int)
@click.option("--task", "-t", type=str, help="New task description")
@click.option("--priority", "-p", type=int, help="New priority (1-3)")
@click.option("--duration", "-d", type=int, help="New duration in minutes")
@click.option("--completed", "-c", type=bool, is_flag=True, help="Mark as completed")
@click.option("--uncompleted", "-u", type=bool, is_flag=True, help="Mark as uncompleted")
def update(list_name: str, id: int, task: str, priority: int, duration: int, completed: bool, uncompleted: bool):
    """Update a todo item."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    todo = get_todo(id)
    if not todo or todo.list_id != lst['id']:
        click.echo(f"Error: Todo with ID {id} not found in list '{list_name}'.")
        return

    if not any([task, priority is None, duration is None, completed, uncompleted]):
         click.echo("Error: Please provide at least one field to update.")
         return

    updates = {"updated_at": datetime.now(timezone.utc).isoformat()}
    if task: updates["task"] = task
    if priority is not None: updates["priority"] = priority
    if duration is not None: updates["duration"] = duration
    if completed: updates["completed"] = True
    elif uncompleted: updates["completed"] = False
    
    update_todo(id, **updates)
    click.echo(f"Successfully updated todo {id} in list '{list_name}'.")