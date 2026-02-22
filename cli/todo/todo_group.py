import click
from .commands.add import add
from .commands.delete import delete
from .commands.update import update
from .commands.view import view

@click.group()
def todo_command():
    """Guide for you to create, read, update, delete and other operations on todos."""
    pass

todo_command.add_command(add)
todo_command.add_command(delete)
todo_command.add_command(update)
todo_command.add_command(view)
