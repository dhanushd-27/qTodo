import click
from core.db import get_all_todo_lists, todo_list_table, Q
from tabulate import tabulate
from utils import format_date

@click.command()
@click.argument("name", type=str, required=False)
def view(name: str):
    """View existing todo lists in the database."""
    if name:
        lst = todo_list_table.get(Q.name == name)
        if lst:
            table = [[lst['id'], lst['name'], lst['description'], format_date(lst.get('created_at')), format_date(lst.get('updated_at'))]]
            headers = ["ID", "Name", "Description", "Created At", "Updated At"]
            click.echo(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            click.echo(f"Error: List '{name}' not found.")
    else:
        lists = get_all_todo_lists()
        if not lists:
            click.echo("No lists found.")
            return
            
        table = [[lst.id, lst.name, lst.description, format_date(lst.created_at), format_date(lst.updated_at)] for lst in lists]
        headers = ["ID", "Name", "Description", "Created At", "Updated At"]
        click.echo(tabulate(table, headers=headers, tablefmt="grid"))