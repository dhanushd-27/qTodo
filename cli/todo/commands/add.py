import click

@click.command()
@click.argument("list", type=str)
@click.argument("todo", type=str)
def add(list: str, todo: str):
    """Add a new todo item."""
    click.echo(f"The todo is {todo} in list {list}")
