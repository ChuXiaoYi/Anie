import datetime

from sqlalchemy import DateTime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime)
    update_time: Mapped[datetime.datetime] = mapped_column(DateTime, onupdate=True)

