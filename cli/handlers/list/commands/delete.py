import click

@click.command()
@click.argument("name", type=str)
def delete(name: str):
    """Delete an existing todo list with confirmation."""

    if click.confirm(f"Are you sure you want to delete the list '{name}'?"):
      click.echo(f"List '{name}' deleted successfully.")
    else:
      click.echo("Deletion cancelled.")
