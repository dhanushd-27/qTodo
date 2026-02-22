import click
from core.db import create_todo_list, todo_list_table, Q as db_Q
from models.todo import TodoList

@click.command()
@click.argument("name", type=str)
@click.option("--desc", type=str, help="Description for the list", default="No description")
def newlist(name: str, desc: str):
    """Create a new list explicitly."""
    if name.startswith("@"):
        name = name[1:]
    
    if todo_list_table.get(db_Q.name == name):
        click.echo(f"Error: List '{name}' already exists.")
        return
        
    create_todo_list(TodoList(name=name, description=desc))
    click.echo(f"List '{name}' created successfully.")
