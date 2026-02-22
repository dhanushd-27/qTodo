import click
import sys
from pathlib import Path

# Add the project root to sys.path
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from cli.commands.add import add
from cli.commands.ls import ls
from cli.commands.done import done
from cli.commands.rm import rm
from cli.commands.lists import lists
from cli.commands.rmlist import rmlist
from cli.commands.switch import switch
from cli.commands.newlist import newlist
from cli.commands.editlist import editlist

@click.group()
def qtodo():
    """qTodo - A simple and fast CLI task manager."""
    pass

# Register commands
qtodo.add_command(add)
qtodo.add_command(ls)
qtodo.add_command(done)
qtodo.add_command(rm)
qtodo.add_command(lists)
qtodo.add_command(rmlist)
qtodo.add_command(switch)
qtodo.add_command(newlist)
qtodo.add_command(editlist)

def main():
    qtodo()

if __name__ == "__main__":
    main()
