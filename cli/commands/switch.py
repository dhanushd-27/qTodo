import click
from config import set_default_list

@click.command()
@click.argument("name", type=str)
def switch(name: str):
    """Switch the default list context."""
    if name.startswith("@"):
        name = name[1:]
    set_default_list(name)
    click.echo(f"Default list switched to '{name}'.")
