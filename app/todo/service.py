import abc

from app.errors.excpetion import NotFoundException, ForbiddenException
from app.todo.repository import BaseTodoRepository
from app.todo.models import TodoInfo


class BaseTodoService(abc.ABC):
    def __init__(self, repository: BaseTodoRepository) -> None:
        self.todo_repository = repository

    @abc.abstractmethod
    async def get_todo_info_list(self, user_id: int) -> list[TodoInfo]:
        raise NotImplementedError

    @abc.abstractmethod
    async def insert_todo(self, user_id: int, context: str) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_todo(self, user_id: int, todo_id: int) -> int:
        raise NotImplementedError


class TodoService(BaseTodoService):
    async def get_todo_info_list(self, user_id: int) -> list[TodoInfo]:
        results = await self.todo_repository.get_todo_info_list(user_id)
        return results

    async def insert_todo(self, user_id: int, context: str) -> TodoInfo:
        result = await self.todo_repository.insert_todo(user_id, context)
        return result

    async def delete_todo(self, user_id: int, todo_id: int) -> str:
        user_validation_check = await self.todo_repository.get_user_id_by_todo_info(
            todo_id
        )

        if user_validation_check == None:
            raise NotFoundException

        elif user_validation_check.user_id != user_id:
            raise ForbiddenException

        result = await self.todo_repository.delete_todo(todo_id)
        if result == 1:
            return "delete success"
        else:
            raise NotImplementedError
