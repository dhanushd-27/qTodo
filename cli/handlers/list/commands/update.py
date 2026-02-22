import click

@click.command()
@click.argument("current_name", type=str)
@click.option("--name", "-n", type=str, help="New name for the list")
@click.option("--description", "-d", type=str, help="New description for the list")
def update(current_name: str, name: str, description: str):
    """Update an existing list with new name and/or description"""
    print(f"Updating list named {current_name} with name {name} and description {description}")
