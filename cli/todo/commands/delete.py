import click
from core.db import delete_todo, get_todo, todo_list_table, Q

@click.command()
@click.argument("list_name", type=str)
@click.argument("id", type=int)
def delete(list_name: str, id: int):
    """Delete a todo item."""
    lst = todo_list_table.get(Q.name == list_name)
    if not lst:
        click.echo(f"Error: List '{list_name}' not found.")
        return
        
    todo = get_todo(id)
    if not todo or todo.list_id != lst['id']:
        click.echo(f"Error: Todo with ID {id} not found in list '{list_name}'.")
        return

    if click.confirm(f"Are you sure you want to delete the todo '{todo.task}' (ID: {id}) from list '{list_name}'?"):
        delete_todo(id)
        click.echo(f"Todo {id} deleted successfully from list '{list_name}'.")
    else:
        click.echo("Deletion cancelled.")