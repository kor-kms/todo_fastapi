import abc

from app.errors.excpetion import NotFoundException
from app.todo.repository import BaseTodoRepository
from app.todo.models import TodoInfo

class BaseTodoService(abc.ABC):
    def __init__(self, repository: BaseTodoRepository) -> None:
        self.todo_repository = repository

    @abc.abstractmethod
    async def getTodoInfoList(self, user_id: int) -> list[TodoInfo]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def insetTodoInfo(self, user_id: int, context: str) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def deleteTodoInfo(self, user_id:int, todo_id: int) -> int:
        raise NotImplementedError

class TodoService(BaseTodoService):
    async def getTodoInfoList(self, user_id: int) -> list[TodoInfo]:
        results = await self.todo_repository.getTodoInfoList(user_id)
        return results
    
    async def insetTodoInfo(self, user_id: int, context: str) -> TodoInfo:
        result = await self.todo_repository.insertTodoInfo(user_id, context)
        return result
    
    async def deleteTodoInfo(self, user_id:int, todo_id: int) -> str:
        result = await self.todo_repository.deleteTodoInfo(user_id, todo_id)
        if result == 1:
            return "DELETE SUCCESS"
        else:
            raise NotFoundException
