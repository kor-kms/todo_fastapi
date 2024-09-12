from fastapi import Depends

from app.depends.repository import get_user_repository, get_todo_repository
from app.user.service import UserService
from app.todo.service import TodoService

def get_user_service(repository=Depends(get_user_repository)):
    return UserService(repository=repository)

def get_todo_service(repository=Depends(get_todo_repository)):
    return TodoService(repository=repository)
