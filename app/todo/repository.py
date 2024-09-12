import abc

from sqlalchemy import select, func, delete
from sqlalchemy.ext.asyncio import AsyncSession
from app.todo.models import MonthInfo, TodoInfo

from app.db import tables as tb


class BaseTodoRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @abc.abstractmethod
    async def getMonthInfo(self, user_id: int, month: int) -> list[MonthInfo]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def getTodoInfo(self, user_id: int, day_id: int) -> list[TodoInfo]:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def insertTodoInfo(self, user_id: int, month: int, day: int, context: str) -> TodoInfo:
        raise NotImplementedError
    
    @abc.abstractmethod
    async def addTodoInfo(self, user_id: int, context: str, day_id: int) -> TodoInfo:
        raise NotImplementedError

    @abc.abstractmethod
    async def deleteTodoInfo(self, todo_id: int, day_id: int) -> int:
        raise NotImplementedError


class TodoRepository(BaseTodoRepository):
    async def getMonthInfo(self, user_id: int, month: int) -> list[MonthInfo]:
        result = (
            (
                await self.session.execute(
                    select(tb.Day)
                    .filter(
                        tb.Day.user_id == user_id,
                        tb.Day.month == month
                    )
                )
            )
            .unique()
            .scalars()
            .all()
        )
        return result
    
    async def getTodoInfo(self, user_id: int, day_id: int) -> list[TodoInfo]:
        result = (
            (
                await self.session.execute(
                    select(tb.Todo)
                    .filter(
                        tb.Todo.user_id == user_id,
                        tb.Todo.day_id == day_id
                    )
                )
            )
            .unique()
            .scalars()
            .all()
        )
        return result
    
    async def insertTodoInfo(self, user_id: int, month: int, day: int, context: str) -> TodoInfo:
        new_day=tb.Day(user_id=user_id, month=month, day=day)
        self.session.add(new_day)
        await self.session.commit()

        new_todo = tb.Todo(user_id=user_id, day_id=new_day.day_id, context=context)
        self.session.add(new_todo)
        await self.session.commit()

        return TodoInfo(
            todo_id = new_todo.todo_id,
            user_id = new_todo.user_id,
            day_id = new_todo.day_id,
            context = new_todo.context,
            created_at = new_todo.created_at,
            modified_at = new_todo.modified_at,
        )

    async def addTodoInfo(self, user_id: int, context: str, day_id: int) -> TodoInfo:
        new_todo = tb.Todo(user_id=user_id, day_id=day_id, context=context)
        self.session.add(new_todo)
        await self.session.flush()
        await self.session.commit()
        
        return TodoInfo(
            todo_id = new_todo.todo_id,
            user_id = new_todo.user_id,
            day_id = new_todo.day_id,
            context = new_todo.context,
            created_at = new_todo.created_at,
            modified_at = new_todo.modified_at,
        )

    async def deleteTodoInfo(self, todo_id: int, day_id: int) -> int:
        countRow = (
            await self.session.execute(
                select(func.count(tb.Todo.todo_id))
                .filter(tb.Todo.day_id == day_id)
            )
        ).scalar_one()

        if countRow == 1:
            await self.session.execute(delete(tb.Todo).where(tb.Todo.todo_id == todo_id))
            await self.session.commit()

            await self.session.execute(delete(tb.Day).where(tb.Day.day_id == day_id))
            await self.session.commit()
        else:
            await self.session.execute(delete(tb.Todo).where(tb.Todo.todo_id == todo_id))
            await self.session.commit()

        return 1

