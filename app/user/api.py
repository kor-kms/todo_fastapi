import os
from datetime import timedelta

from dotenv import load_dotenv
from fastapi import APIRouter, Body, Depends, HTTPException, Response, status
from jose import jwt

from app.depends.service import get_user_service
from app.user.models import Token, UserLoginResquest
from app.user.service import BaseUserService

# from app.utils.jwt import create_access_token


load_dotenv()
# ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app_router = APIRouter()


@app_router.post(path="/login")
async def user_login(
    body: UserLoginResquest, user_svc: BaseUserService = Depends(get_user_service)
):
    res = await user_svc.get_user(id, pw)
    return {"token": res[0], "user": res[1]}
