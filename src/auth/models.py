from datetime import datetime
from sqlalchemy import (Boolean,
                        Integer,
                        String,
                        TIMESTAMP,
                        ForeignKey,
                        Table,
                        Column,
                        JSON)
from fastapi_users.db import SQLAlchemyBaseUserTable
from database import Base, metadata
from sqlalchemy.orm import Mapped, mapped_column


# Таблица с ролями пользователя
role = Table(
    'role',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permissions", JSON),
)


class User(SQLAlchemyBaseUserTable[int], Base):
    """Переопределенная таблица пользователя, добавил поле role_id """
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False, unique=True)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, ForeignKey(role.c.id))
    hashed_password: Mapped[str] = mapped_column(
        String(length=1024), nullable=False
    )
    is_active: Mapped[bool] = mapped_column(Boolean,
                                            default=True,
                                            nullable=False)
    is_superuser: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
    is_verified: Mapped[bool] = mapped_column(
        Boolean, default=False, nullable=False
    )
