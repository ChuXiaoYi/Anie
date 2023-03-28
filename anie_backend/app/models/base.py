import datetime

from sqlalchemy import DateTime, func, SmallInteger
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(autoincrement=True, primary_key=True)
    create_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    update_time: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    status: Mapped[int] = mapped_column(SmallInteger, default=1, comment="状态 1:正常 0:删除")

    def to_dicts(self) -> dict:
        """

        :rtype: object
        """
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

