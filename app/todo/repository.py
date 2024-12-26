import abc

from sqlalchemy import select, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.todo.models import TodoInfo

from app.db import tables as tb


class BaseTodoRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @abc.abstractmethod
    async def get_todo_info_list(self, user_id: int) -> list[TodoInfo]:
        raise NotImplementedError

    @abc.abstractmethod
    async def get_user_id_by_todo_info(self, todo_id: int) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def insert_todo(self, user_id: int, context: str) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def delete_todo(self, todo_id: int) -> int:
        raise NotImplementedError


class TodoRepository(BaseTodoRepository):
    async def get_todo_info_list(self, user_id: int) -> list[TodoInfo]:
        results = (
            (
                await self.session.execute(
                    select(tb.Todo).filter(tb.Todo.user_id == user_id)
                )
            )
            .unique()
            .scalars()
            .all()
        )
        return [TodoInfo.model_validate(row) for row in results]

    async def get_user_id_by_todo_info(self, todo_id: int) -> TodoInfo:
        result = (
            (
                await self.session.execute(
                    select(tb.Todo).filter(tb.Todo.todo_id == todo_id)
                )
            )
            .unique()
            .scalar_one_or_none()
        )
        return result

    async def insert_todo(self, user_id: int, context: str) -> TodoInfo:
        new_todo = tb.Todo(user_id=user_id, context=context)
        self.session.add(new_todo)
        await self.session.commit()

        return TodoInfo(
            todo_id=new_todo.todo_id,
            user_id=new_todo.user_id,
            context=new_todo.context,
            created_at=new_todo.created_at,
            modified_at=new_todo.modified_at,
        )

    async def delete_todo(self, todo_id: int) -> str:
        result = await self.session.execute(
            delete(tb.Todo).where(tb.Todo.todo_id == todo_id)
        )
        await self.session.commit()

        return result.rowcount
