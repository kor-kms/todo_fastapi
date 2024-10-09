from typing import Union

from fastapi import Request
from fastapi.exceptions import RequestValidationError
from fastapi.openapi.constants import REF_PREFIX
from fastapi.openapi.utils import validation_error_response_definition
from fastapi.responses import JSONResponse
from starlette.status import HTTP_404_NOT_FOUND

from app.errors.excpetion import UserIdNotFoundError


async def http404_error_handler(
    _: Request,
    exc: RequestValidationError | UserIdNotFoundError,
) -> JSONResponse:
    return JSONResponse(
        {"errors": exc.errors()},
        status_code=HTTP_404_NOT_FOUND,
    )


validation_error_response_definition["properties"] = {
    "errors": {
        "title": "Errors",
        "type": "array",
        "items": {"$ref": "{0}ValidationError".format(REF_PREFIX)},
    },
}
