from dotenv import load_dotenv
from fastapi import APIRouter, Depends

from app.depends.service import get_user_service
from app.user.models import UserLoginResquest
from app.user.service import BaseUserService

load_dotenv()

app_router = APIRouter()

@app_router.post(path="/login")
async def user_login(
    body: UserLoginResquest, user_svc: BaseUserService = Depends(get_user_service)
):
    res = await user_svc.get_user(body.id, body.pw)
    return res
