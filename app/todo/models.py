import datetime
import uuid

from pydantic import BaseModel, ConfigDict

class Base(BaseModel):
    model_config = ConfigDict(from_attributes=True, frozen=True)

class MonthInfo(Base):
    day_id: int
    user_id: int
    month: int
    day: int
    created_at: datetime.datetime
    modified_at: datetime.datetime

class GetMonthInfoList(BaseModel):
    data: list[MonthInfo]

class TodoInfo(Base):
    todo_id: int
    user_id: int
    day_id: int
    context: str
    created_at: datetime.datetime
    modified_at: datetime.datetime

class GetTodoInfoList(BaseModel):
    data: list[TodoInfo]

class GetTodoInfo(BaseModel):
    data: TodoInfo

class InsertTodoInfo(GetTodoInfo):
    pass

class DeleteTodoCount(BaseModel):
    data: int

class DeleteTodoInfo(DeleteTodoCount):
    pass

