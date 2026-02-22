import click

@click.command()
@click.argument("list", type=str)
@click.argument("todo", type=str)
@click.argument("new_todo", type=str)
def update(list: str, todo: str, new_todo: str):
    """Update a todo item."""
    click.echo(f"The todo is {todo} in list {list}")