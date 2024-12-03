import abc

from app.errors.excpetion import UnAuthorizedException, NotFoundException
from app.user.models import UserLoginResponse
from app.user.repository import BaseUserRepository
from app.depends.auth import get_token

from cryptography.fernet import Fernet

secret_key = Fernet.generate_key()
cipher_suite = Fernet(secret_key)

class BaseUserService(abc.ABC):
    def __init__(self, repository: BaseUserRepository) -> None:
        self.user_repository = repository

    @abc.abstractmethod
    async def get_user(self, id: str, pw: str) -> UserLoginResponse:
        raise NotImplementedError


class UserService(BaseUserService):
    async def get_user(self, id: str, pw: str) -> UserLoginResponse:
        user = await self.user_repository.findUser(id)
        if not user:
            raise NotFoundException

        if user.pw != pw:
            raise UnAuthorizedException
        
        cipher_token = await get_token(user.user_id)

        return (
            UserLoginResponse(
                token=cipher_token,
                nickname=user.id,
            )
        )
