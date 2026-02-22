import click

@click.command()
@click.argument("name", type=str)
@click.argument("description", type=str, required=False)
def create(name: str, description: str):
    """Create a new list with name and description"""
    print(f"Creating a new list named {name} with description {description}")