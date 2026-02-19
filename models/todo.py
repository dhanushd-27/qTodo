from uuid import uuid4
from pydantic import BaseModel, Field
from typing import List
from datetime import datetime, timezone

class Todo(BaseModel):
  id: str = Field(default_factory=lambda: str(uuid4()))
  task: str
  priority: int = Field(default=2, ge=1, le=3)
  duration: int = Field(default=60, gt=0)
  completed: bool = False
  created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))


class TodoList(BaseModel):
  id: str = Field(default_factory=lambda: str(uuid4()))
  name: str
  description: str
  created_at: datetime = Field(default_factory=datetime.now(timezone.utc))
  updated_at: datetime = Field(default_factory=datetime.now(timezone.utc))
  todos: List[Todo] = Field(default_factory=list)