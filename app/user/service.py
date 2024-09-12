import abc

from app.user.repository import BaseUserRepository

class BaseUserService(abc.ABC):
    def __init__(self, repository: BaseUserRepository) -> None:
        self.user_repository = repository

    @abc.abstractmethod
    async def findUser(self, id: str) -> str:
        raise NotImplementedError

    @abc.abstractmethod
    async def verifyPassword(self, id: str, pw: str) -> bool:
        raise NotImplementedError


class UserService(BaseUserService):
    async def findUser(self, id: str) -> str:
        results = await self.user_repository.findUser(id)
        return results

    async def verifyPassword(self, id: str, pw: str) -> bool:
        results = await self.user_repository.verifyPassword(id, pw)
        return results
