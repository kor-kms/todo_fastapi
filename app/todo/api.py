from fastapi import APIRouter, Depends

from app.depends.auth import get_current_user
from app.depends.service import get_todo_service
from app.todo.models import (
    DeleteTodo,
    DeleteTodoInfo,
    GetTodoInfo,
    GetTodoInfoList,
    InsertTodoInfo,
)
from app.todo.service import BaseTodoService

app_router = APIRouter()


@app_router.get("/todo", response_model=GetTodoInfoList)
async def get_todo_info_list(
    user_id: int = Depends(get_current_user),
    todo_svc: BaseTodoService = Depends(get_todo_service),
):
    todoinfo = await todo_svc.get_todo_info_list(user_id)
    return GetTodoInfoList(data=todoinfo)


@app_router.post("/todo", response_model=InsertTodoInfo, status_code=201)
async def insert_todo(
    context: str,
    user_id: int = Depends(get_current_user),
    todo_svc: BaseTodoService = Depends(get_todo_service),
):
    todoinfo = await todo_svc.insert_todo(user_id, context)
    return GetTodoInfo(data=todoinfo)


@app_router.delete("/todo", response_model=DeleteTodoInfo)
async def delete_todo(
    todo_id: int,
    user_id: int = Depends(get_current_user),
    todo_svc: BaseTodoService = Depends(get_todo_service),
):
    deleteinfo = await todo_svc.delete_todo(user_id, todo_id)
    return DeleteTodo(data=deleteinfo)
