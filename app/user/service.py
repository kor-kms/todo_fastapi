import abc
from datetime import datetime
from typing import Tuple

from app.errors.excpetion import NotAuthenticated, UserIdNotFoundError
from app.user.models import Token, UserLoginResponse
from app.user.repository import BaseUserRepository


class BaseUserService(abc.ABC):
    def __init__(self, repository: BaseUserRepository) -> None:
        self.user_repository = repository

    @abc.abstractmethod
    async def get_user(self, id: str, pw: str) -> Token:
        raise NotImplementedError


class UserService(BaseUserService):
    async def get_user(self, id: str, pw: str) -> Tuple[Token, UserLoginResponse]:
        user = await self.user_repository.findUser(id)
        if not user:
            raise UserIdNotFoundError

        if user.pw != pw:
            raise NotAuthenticated

        token = await self._get_token(id)

        return (
            token,
            UserLoginResponse(
                id=user.id,
                nickname=user.nickname,
                time_created=user.time_created,
            ),
        )

    async def _get_token(self, id: str) -> Token:
        return f"{id}-Simple-token-{datetime.now()}"
