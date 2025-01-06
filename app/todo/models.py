import datetime

from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)

class TodoInfo(Base):
    todo_id: int
    user_id: int
    context: str
    created_at: datetime.datetime
    modified_at: datetime.datetime | None

class GetTodoInfoList(BaseModel):
    data: list[TodoInfo]

class GetTodoInfo(BaseModel):
    data: TodoInfo

class InsertTodoInfo(GetTodoInfo):
    pass

class DeleteTodo(BaseModel):
    data: str

class DeleteTodoInfo(DeleteTodo):
    pass

