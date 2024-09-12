from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.session import SessionManager

async def get_session() -> AsyncGenerator[AsyncSession, None]:
    session_manager = SessionManager()
    async with session_manager.async_session() as async_session:
        yield async_session
