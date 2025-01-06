from fastapi import Depends

from app.depends.db import get_session
from app.user.repository import BaseUserRepository, UserRepository
from app.todo.repository import BaseTodoRepository, TodoRepository

def get_user_repository(session=Depends(get_session)) -> BaseUserRepository:
    return UserRepository(session=session)

def get_todo_repository(session=Depends(get_session)) -> BaseTodoRepository:
    return TodoRepository(session=session)
