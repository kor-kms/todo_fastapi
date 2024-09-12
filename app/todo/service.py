import abc

from app.todo.repository import BaseTodoRepository
from app.todo.models import MonthInfo, TodoInfo

class BaseTodoService(abc.ABC):
    def __init__(self, repository: BaseTodoRepository) -> None:
        self.todo_repository = repository

    @abc.abstractmethod
    async def getMonthInfo(self, user_id: int, month: int) -> list[MonthInfo]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def getTodoInfo(self, user_id: int, day_id: int) -> list[TodoInfo]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def insetTodoInfo(self, user_id: int, month: int, day: int, context: str, day_id: int) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def deleteTodoInfo(self, todo_id: int, day_id: int) -> int:
        raise NotImplementedError

class TodoService(BaseTodoService):
    async def getMonthInfo(self, user_id: int, month: int) -> list[MonthInfo]:
        results = await self.todo_repository.getMonthInfo(user_id, month)
        return results
    
    async def getTodoInfo(self, user_id: int, day_id: int) -> list[TodoInfo]:
        results = await self.todo_repository.getTodoInfo(user_id, day_id)
        return results
    
    async def insetTodoInfo(self, user_id: int, month: int, day: int, context: str, day_id: int) -> TodoInfo:
        if day_id == 0:
            results = await self.todo_repository.insertTodoInfo(user_id, month, day, context)
        else:
            results = await self.todo_repository.addTodoInfo(user_id, context, day_id)
        return results
    
    async def deleteTodoInfo(self, todo_id: int, day_id: int) -> int:
        results = await self.todo_repository.deleteTodoInfo(todo_id, day_id)
        return results
