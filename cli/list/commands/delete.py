import click
from core.db import delete_todo_list, todo_list_table, Q

@click.command()
@click.argument("name", type=str)
def delete(name: str):
    """Delete an existing todo list with confirmation."""
    lst = todo_list_table.get(Q.name == name)
    if not lst:
        click.echo(f"Error: List '{name}' not found.")
        return

    if click.confirm(f"Are you sure you want to delete the list '{name}'?"):
        delete_todo_list(lst['id'])
        click.echo(f"List '{name}' deleted successfully.")
    else:
        click.echo("Deletion cancelled.")

