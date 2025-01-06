import datetime
from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base

class User(Base):
    user_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    id: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )
    pw: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now()
    )
    modified_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    
    __tablename__ = "TB_USER"


class Todo(Base):
    todo_id: Mapped[int] = Column(Integer, primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Integer, nullable=False)
    context: Mapped[str] = mapped_column(String, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now()
    )
    modified_at: Mapped[datetime.datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )
    
    __tablename__ = "TB_TODO"