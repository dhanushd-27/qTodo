import click
from models.todo import TodoList
from core.db import create_todo_list, todo_list_table, Q

@click.command()
@click.argument("name", type=str)
@click.argument("description", type=str, required=False)
def create(name: str, description: str):
    """Create a new list with name and description"""
    if todo_list_table.get(Q.name == name):
        click.echo(f"Error: List with name '{name}' already exists.")
        return
        
    desc = description if description else "No description"
    new_list = TodoList(name=name, description=desc)
    create_todo_list(new_list)
    click.echo(f"Successfully created a new list named '{name}'.")