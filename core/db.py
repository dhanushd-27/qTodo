from tinydb import TinyDB, Query
from models.todo import Todo, TodoList
from typing import Optional

db = TinyDB("todos.json")
todo_list_table = db.table("todo_list")
todo_table = db.table("todo")

Q = Query()


# ── TodoList CRUD ──

def get_next_id(table) -> int:
    docs = table.all()
    if not docs:
        return 1
    return max(doc.get("id", 0) for doc in docs) + 1


def create_todo_list(todo_list: TodoList) -> TodoList:
    if todo_list.id is None:
        todo_list.id = get_next_id(todo_list_table)
    todo_list_table.insert(todo_list.model_dump(mode="json"))
    return todo_list


def get_all_todo_lists() -> list[TodoList]:
    return [TodoList(**row) for row in todo_list_table.all()]


def get_todo_list(list_id: int) -> Optional[TodoList]:
    row = todo_list_table.get(Q.id == list_id)
    return TodoList(**row) if row else None


def update_todo_list(list_id: int, **fields) -> Optional[TodoList]:
    todo_list_table.update(fields, Q.id == list_id)
    return get_todo_list(list_id)


def delete_todo_list(list_id: int) -> bool:
    removed = todo_list_table.remove(Q.id == list_id)
    if removed:
        todo_table.remove(Q.list_id == list_id)
    return len(removed) > 0


# ── Todo CRUD ──

def create_todo(list_id: int, todo: Todo) -> Todo:
    if todo.id is None:
        todo.id = get_next_id(todo_table)
    data = todo.model_dump(mode="json")
    data["list_id"] = list_id
    todo_table.insert(data)
    return todo


def get_all_todos(list_id: int) -> list[Todo]:
    rows = todo_table.search(Q.list_id == list_id)
    return [Todo(**row) for row in rows]


def get_todo(todo_id: int) -> Optional[Todo]:
    row = todo_table.get(Q.id == todo_id)
    return Todo(**row) if row else None


def update_todo(todo_id: int, **fields) -> Optional[Todo]:
    todo_table.update(fields, Q.id == todo_id)
    return get_todo(todo_id)


def toggle_todo(todo_id: int) -> Optional[Todo]:
    todo = get_todo(todo_id)
    if not todo:
        return None
    todo_table.update({"completed": not todo.completed}, Q.id == todo_id)
    return get_todo(todo_id)


def delete_todo(todo_id: int) -> bool:
    removed = todo_table.remove(Q.id == todo_id)
    return len(removed) > 0