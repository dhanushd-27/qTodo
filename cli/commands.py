import click
import sys
from pathlib import Path

# Add the project root to sys.path to resolve 'models' and 'core' imports
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from cli.list.list_group import list_command
from cli.todo.todo_group import todo_command

@click.group()
def qtodo():
    pass

qtodo.add_command(list_command, name="list")
qtodo.add_command(todo_command, name="todo")

def main():
    qtodo()

if __name__ == "__main__":
    main()