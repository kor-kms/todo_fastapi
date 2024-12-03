from fastapi import APIRouter, Depends

from app.depends.auth import get_current_user
from app.depends.service import get_todo_service
from app.todo.models import (DeleteTodo, DeleteTodoInfo,
                             GetTodoInfo, GetTodoInfoList, InsertTodoInfo)
from app.todo.service import BaseTodoService

app_router = APIRouter()


@app_router.get("/todoinfo", response_model=GetTodoInfoList)
async def getTodoInfoList(
    user_id: int = Depends(get_current_user), todo_svc: BaseTodoService = Depends(get_todo_service),
):
    todoinfo = await todo_svc.getTodoInfoList(user_id)
    return GetTodoInfoList(data=todoinfo)


@app_router.post("/regtodo", response_model=InsertTodoInfo, status_code=201)
async def insertTodo(
    context: str, user_id: int = Depends(get_current_user), todo_svc: BaseTodoService = Depends(get_todo_service),
):
    todoinfo = await todo_svc.insetTodoInfo(user_id, context)
    return GetTodoInfo(data=todoinfo)


@app_router.post("/deltodo", response_model=DeleteTodoInfo)
async def deleteTodo(
    todo_id: int, user_id: int =  Depends(get_current_user), todo_svc: BaseTodoService = Depends(get_todo_service),
):
    deleteinfo = await todo_svc.deleteTodoInfo(user_id, todo_id)
    return DeleteTodo(data=deleteinfo)




