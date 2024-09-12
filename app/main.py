from fastapi import APIRouter, FastAPI
from app.user import api as user_api
from app.todo import api as todo_api
#from app.utils import JWTMiddleware

def get_application() -> FastAPI:
    application = FastAPI()
#    application.add_middleware(JWTMiddleware)
    api_router = APIRouter()
    api_router.include_router(user_api.app_router, prefix="/user", tags=["user"])
    api_router.include_router(todo_api.app_router, prefix="/todo", tags=["todo"])
    application.include_router(api_router)

    return application

app = get_application()