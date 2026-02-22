import click
from core.db import delete_todo_list, todo_list_table, Q as db_Q
from config import get_default_list, set_default_list

@click.command()
@click.argument("name", type=str)
def rmlist(name: str):
    """Remove an entire list and all its tasks."""
    if name.startswith("@"):
        name = name[1:]
    lst = todo_list_table.get(db_Q.name == name)
    if not lst:
        click.echo(f"Error: List '{name}' not found.")
        return
    
    if delete_todo_list(lst['id']):
        click.echo(f"List '{name}' and all its tasks have been deleted.")
        if get_default_list() == name:
            set_default_list("Inbox")
    else:
        click.echo(f"Failed to delete list '{name}'.")
