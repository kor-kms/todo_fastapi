from fastapi import Request
from fastapi.responses import JSONResponse

from app.errors.excpetion import NotFoundException


async def not_fount_exception_handler (request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404, content={"message": f"DATA NOT FOUND"}
    )


async def un_authorized_exception_handler (request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=401, content={"message": f"UNAUTHORIZED"}
    )


async def forbidden_exception_handler (request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=403, content={"message": f"FORBIDDEN"}
    )