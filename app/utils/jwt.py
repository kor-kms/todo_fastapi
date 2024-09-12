from datetime import datetime
from datetime import timedelta
from jose import jwt
from fastapi import Request, HTTPException, status
from fastapi.middleware.base import BaseHTTPMiddleware

import os
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

class JWTMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        """  # JWT 검사가 필요 없는 경로
        exempt_paths = ["/user/ping", "/user/you"]

        # wildcard 경로 처리
        if any(request.url.path.startswith(path) or request.url.path.startswith(path[:-1]) for path in exempt_paths):
            return await call_next(request) """
        
        token = request.headers.get("Authorization")
        if token:
            token = token.split(" ")[1]
            try:
                jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            except:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Invalid token"})
        else:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, content={"message": "Token missing"})
        
        return await call_next(request)