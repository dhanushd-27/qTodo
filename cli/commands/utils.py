from core.db import create_todo_list, todo_list_table, Q as db_Q
from models.todo import TodoList
from config import get_default_list

def resolve_list(list_identifier: str | None) -> tuple[int, str]:
    """Helper to resolve list name to ID, creating it if it doesn't exist."""
    name = list_identifier or get_default_list()
    if name.startswith("@"):
        name = name[1:]
    
    lst = todo_list_table.get(db_Q.name == name)
    if not lst:
        nl = create_todo_list(TodoList(name=name, description="Auto-generated list"))
        return nl.id, nl.name
    return lst['id'], lst['name']
