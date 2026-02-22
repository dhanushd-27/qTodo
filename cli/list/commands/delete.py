import click
from core.db import delete_todo_list, todo_list_table, Q, get_todo_list

@click.command()
@click.argument("id", type=int)
def delete(id: int):
    """Delete an existing todo list with confirmation."""
    lst = get_todo_list(id)
    if not lst:
        click.echo(f"Error: List '{id}' not found.")
        return

    if click.confirm(f"Are you sure you want to delete the list '{lst.name}'?"):
        delete_todo_list(lst.id)
        click.echo(f"List '{lst.name}' deleted successfully.")
    else:
        click.echo("Deletion cancelled.")

