import click
from core.db import get_all_todo_lists
from tabulate import tabulate

@click.command()
def lists():
    """View all lists."""
    lists = get_all_todo_lists()
    if not lists:
        click.echo("No lists found.")
        return
        
    table = [[lst.name, lst.description] for lst in lists]
    headers = ["Name", "Description"]
    click.echo(tabulate(table, headers=headers, tablefmt="simple"))
