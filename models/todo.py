from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timezone

class Todo(BaseModel):
  id: int | None = Field(default=None)
  task: str
  priority: int = Field(default=2, ge=1, le=3)
  duration: int = Field(default=60, gt=0)
  completed: bool = False
  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class TodoList(BaseModel):
  id: int | None = Field(default=None)
  name: str
  description: str
  created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
  todos: List[Todo] = Field(default_factory=list)