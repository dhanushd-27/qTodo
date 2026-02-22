import click

@click.command()
@click.argument("list", type=str)
def view(list: str):
    """View todos in a list."""
    click.echo(f"The todos in list {list}")