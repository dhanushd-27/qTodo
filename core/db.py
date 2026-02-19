from tinydb import TinyDB, Query
from models.todo import Todo, TodoList
from typing import Optional

db = TinyDB("todos.json")
todo_list_table = db.table("todo_list")
todo_table = db.table("todo")

Q = Query()


# ── TodoList CRUD ──

def create_todo_list(todo_list: TodoList) -> TodoList:
    todo_list_table.insert(todo_list.model_dump(mode="json"))
    return todo_list


def get_all_todo_lists() -> list[TodoList]:
    return [TodoList(**row) for row in todo_list_table.all()]


def get_todo_list(list_id: str) -> Optional[TodoList]:
    row = todo_list_table.get(Q.id == list_id)
    return TodoList(**row) if row else None


def update_todo_list(list_id: str, **fields) -> Optional[TodoList]:
    todo_list_table.update(fields, Q.id == list_id)
    return get_todo_list(list_id)


def delete_todo_list(list_id: str) -> bool:
    removed = todo_list_table.remove(Q.id == list_id)
    if removed:
        todo_table.remove(Q.list_id == list_id)
    return len(removed) > 0


# ── Todo CRUD ──

def create_todo(list_id: str, todo: Todo) -> Todo:
    data = todo.model_dump(mode="json")
    data["list_id"] = list_id
    todo_table.insert(data)
    return todo


def get_all_todos(list_id: str) -> list[Todo]:
    rows = todo_table.search(Q.list_id == list_id)
    return [Todo(**row) for row in rows]


def get_todo(todo_id: str) -> Optional[Todo]:
    row = todo_table.get(Q.id == todo_id)
    return Todo(**row) if row else None


def update_todo(todo_id: str, **fields) -> Optional[Todo]:
    todo_table.update(fields, Q.id == todo_id)
    return get_todo(todo_id)


def toggle_todo(todo_id: str) -> Optional[Todo]:
    todo = get_todo(todo_id)
    if not todo:
        return None
    todo_table.update({"completed": not todo.completed}, Q.id == todo_id)
    return get_todo(todo_id)


def delete_todo(todo_id: str) -> bool:
    removed = todo_table.remove(Q.id == todo_id)
    return len(removed) > 0