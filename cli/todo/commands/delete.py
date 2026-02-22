import click

@click.command()
@click.argument("list", type=str)
@click.argument("id", type=str)
def delete(list: str, id: str):
    """Delete a todo item."""
    if click.confirm(f"Are you sure you want to delete the todo '{id}' from list '{list}'?"):
        click.echo(f"The todo is {id} in list {list}")
    else:
        click.echo("Deletion cancelled.")