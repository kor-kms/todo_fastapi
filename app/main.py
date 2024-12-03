from fastapi import APIRouter, FastAPI

from app.errors.handlers import not_fount_exception_handler, un_authorized_exception_handler, forbidden_exception_handler
from app.errors.excpetion import NotFoundException, UnAuthorizedException, ForbiddenException
from app.todo import api as todo_api
from app.user import api as user_api

def get_application() -> FastAPI:
    application = FastAPI()
    api_router = APIRouter()
    api_router.include_router(user_api.app_router, prefix="/user", tags=["user"])
    api_router.include_router(todo_api.app_router, prefix="/todo", tags=["todo"])
    application.include_router(api_router)

    application.add_exception_handler(NotFoundException, not_fount_exception_handler)
    application.add_exception_handler(UnAuthorizedException, un_authorized_exception_handler)
    application.add_exception_handler(ForbiddenException, forbidden_exception_handler)

    return application

app = get_application()

