from fastapi import APIRouter, Depends, status, HTTPException, Response

from app.user.models import UserLoginResquest, Token
from app.depends.service import get_user_service
from app.user.service import BaseUserService

from datetime import timedelta
from jose import jwt
#from app.utils.jwt import create_access_token

import os
from dotenv import load_dotenv

load_dotenv()
#ACCESS_TOKEN_EXPIRE_MINUTES = float(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

app_router = APIRouter()

@app_router.get(path="/ping")
def index():
    return {"message": "Hello World"}

""" @app_router.post(path="/login")
async def login(response: Response, login_form: UserLoginResquest, user_svc: BaseUserService = Depends(get_user_service)):
    # 회원 존재 여부 확인
    userValidationCheck = await user_svc.findUser(login_form.id)

    if userValidationCheck == None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid ID")
    
    # 비밀번호 체크
    pwValidationCheck = await user_svc.verifyPassword(login_form.id, login_form.pw)

    if pwValidationCheck == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid password")

    # 토큰 생성
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": login_form.id}, expires_delta=access_token_expires)

    # 쿠키에 저장
    response.set_cookie(key="access_token", value=access_token, expires=access_token_expires, httponly=True)

    return Token(access_token=access_token, token_type="bearer") """
