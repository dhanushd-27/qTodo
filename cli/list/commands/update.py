import click
from core.db import update_todo_list, todo_list_table, Q
from datetime import datetime, timezone

@click.command()
@click.argument("id", type=str)
@click.option("--name", "-n", type=str, help="New name for the list")
@click.option("--description", "-d", type=str, help="New description for the list")
def update(id: str, name: str, description: str):
    """Update an existing list with new name and/or description"""
    lst = todo_list_table.get(Q.id == id)
    if not lst:
        click.echo(f"Error: List '{current_name}' not found.")
        return
        
    if not name and not description:
        click.echo("Error: Please provide at least one value to update (--name or --description).")
        return
        
    updates = {"updated_at": datetime.now(timezone.utc).isoformat()}
    if name:
        updates["name"] = name
    if description:
        updates["description"] = description
        
    update_todo_list(lst['id'], **updates)
    click.echo(f"Successfully updated list '{current_name}'.")
