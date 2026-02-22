import click

@click.command()
@click.argument("list", type=str)
@click.argument("todo", type=str)
def delete(list: str, todo: str):
    """Delete a todo item."""
    if click.confirm(f"Are you sure you want to delete the todo '{todo}' from list '{list}'?"):
        click.echo(f"The todo is {todo} in list {list}")
    else:
        click.echo("Deletion cancelled.")