from fastapi import APIRouter, Depends, status, HTTPException, Response

from app.depends.service import get_todo_service
from app.todo.service import BaseTodoService
from app.todo.models import GetMonthInfoList, GetTodoInfoList, InsertTodoInfo, GetTodoInfo, DeleteTodoInfo, DeleteTodoCount

app_router = APIRouter()

@app_router.get("/monthinfo", response_model=GetMonthInfoList)
async def getMonthInfo(
    user_id: int, month: int, todo_svc: BaseTodoService = Depends(get_todo_service)
):
    dayinfo = await todo_svc.getMonthInfo(user_id, month)
    return GetMonthInfoList(data=dayinfo)

@app_router.get("/todoinfo", response_model=GetTodoInfoList)
async def getTodoInfo(
    user_id: int, day_id: int, todo_svc: BaseTodoService = Depends(get_todo_service)
):
    todoinfo = await todo_svc.getTodoInfo(user_id, day_id)
    return GetTodoInfoList(data=todoinfo)

@app_router.post("/regtodo", response_model=InsertTodoInfo, status_code=201)
async def insertTodo(
    user_id: int, month: int, day: int, context: str, day_id: int, todo_svc: BaseTodoService = Depends(get_todo_service)
):
    todoinfo = await todo_svc.insetTodoInfo(user_id, month, day, context, day_id)
    return GetTodoInfo(data=todoinfo)

@app_router.post("/deltodo", response_model=DeleteTodoInfo)
async def deleteTodo(
    todo_id: int, day_id: int, todo_svc: BaseTodoService = Depends(get_todo_service)
):
    deleteinfo = await todo_svc.deleteTodoInfo(todo_id, day_id)
    return DeleteTodoCount(data=deleteinfo)