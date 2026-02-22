import click
from core.db import get_all_todo_lists, todo_list_table, Q
from tabulate import tabulate

@click.command()
@click.argument("name", type=str, required=False)
def view(name: str):
    """View existing todo lists in the database."""
    if name:
        lst = todo_list_table.get(Q.name == name)
        if lst:
            table = [[lst['name'], lst['description'], lst['created_at'], lst['updated_at']]]
            headers = ["Name", "Description", "Created At", "Updated At"]
            click.echo(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            click.echo(f"Error: List '{name}' not found.")
    else:
        lists = get_all_todo_lists()
        if not lists:
            click.echo("No lists found.")
            return
            
        table = [[lst.name, lst.description, lst.created_at.strftime("%Y-%m-%d %H:%M:%S") if hasattr(lst.created_at, 'strftime') else lst.created_at] for lst in lists]
        headers = ["Name", "Description", "Created At"]
        click.echo(tabulate(table, headers=headers, tablefmt="grid"))