from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(255), comment="用户名")
    email: Mapped[str] = mapped_column(String(255), comment="邮箱")
    phone: Mapped[str] = mapped_column(String(11), comment="电话号码")

