from asyncio import current_task
from contextlib import asynccontextmanager
from typing import AsyncGenerator
from pydantic import PostgresDsn

from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_scoped_session,
    async_sessionmaker,
    create_async_engine,
)


class SessionManager:
    def __init__(self):
        self._engine = create_async_engine(
            "postgresql+asyncpg://user:password@127.0.0.1:5432/todo",
            pool_size=10,
            max_overflow=10,
            echo=True,
        )
        self._async_session_factory = async_scoped_session(
            async_sessionmaker(
                self._engine,
                expire_on_commit=False,
                autoflush=False,
            ),
            scopefunc=current_task,
        )

    @property
    def engine(self):
        return self._engine

    @asynccontextmanager
    async def async_session(self) -> AsyncGenerator[AsyncSession, None]:
        session = self._async_session_factory()
        try:
            yield session
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
