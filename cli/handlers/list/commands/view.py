import click

@click.command()
@click.argument("name", type=str)
def view(name: str):
    """View existing todo lists in the database."""
    print(f"Viewing lists named {name}")