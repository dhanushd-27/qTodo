import click
from core.db import todo_list_table, Q as db_Q, update_todo_list
from config import get_default_list, set_default_list
from datetime import datetime, timezone

@click.command()
@click.argument("old_name", type=str)
@click.argument("new_name", type=str)
@click.option("--desc", type=str, help="New description for the list")
def editlist(old_name: str, new_name: str, desc: str):
    """Update a list's name and/or description."""
    if old_name.startswith("@"):
        old_name = old_name[1:]
    if new_name.startswith("@"):
        new_name = new_name[1:]
        
    lst = todo_list_table.get(db_Q.name == old_name)
    if not lst:
        click.echo(f"Error: List '{old_name}' not found.")
        return
        
    updates = {"updated_at": datetime.now(timezone.utc).isoformat()}
    if new_name and new_name != old_name:
        if todo_list_table.get(db_Q.name == new_name):
            click.echo(f"Error: A list with name '{new_name}' already exists.")
            return
        updates["name"] = new_name
        
        # update default config if it was old_name
        if get_default_list() == old_name:
            set_default_list(new_name)
            
    if desc:
        updates["description"] = desc
        
    update_todo_list(lst['id'], **updates)
    click.echo(f"Successfully updated list '{old_name}'.")
