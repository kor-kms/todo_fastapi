import abc

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, lazyload

from app.db import tables as tb


class BaseUserRepository(abc.ABC):
    def __init__(self, session: AsyncSession) -> None:
        self.session = session

    @abc.abstractmethod
    async def findUser(self, id: str) -> str:
        raise NotImplementedError


class UserRepository(BaseUserRepository):
    async def findUser(self, id: str) -> str:
        result = (
            (await self.session.execute(select(tb.User).filter(tb.User.id == id)))
            .unique()
            .scalar_one_or_none()
        )

        return result
