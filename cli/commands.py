import click
from cli.handlers.list.list_group import list_command
from cli.handlers.todo.todo_group import todo_command

@click.group()
def qtodo():
    pass

qtodo.add_command(list_command, name="list")
qtodo.add_command(todo_command, name="todo")

def main():
    qtodo()