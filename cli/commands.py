import click
from cli.handlers.list.list_group import list_command

@click.group()
def qtodo():
    pass

qtodo.add_command(list_command, name="list")

def main():
    qtodo()