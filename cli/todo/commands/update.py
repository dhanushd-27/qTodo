import click

@click.command()
@click.argument("list", type=str)
@click.argument("id", type=str)
@click.argument("new_todo", type=str)
def update(list: str, id: str, new_todo: str):
    """Update a todo item."""
    click.echo(f"The todo is {todo} in list {list}")