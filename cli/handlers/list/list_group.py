import click
from .commands.create import create
from .commands.view import view
from .commands.update import update
from .commands.delete import delete

@click.group()
def list_command():
    """Guide for you to create, read, update, delete and other operations on lists."""
    pass

list_command.add_command(create)
list_command.add_command(view)
list_command.add_command(update)
list_command.add_command(delete)
