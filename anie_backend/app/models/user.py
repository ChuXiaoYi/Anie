from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class User(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(255), comment="用户名")
    password: Mapped[str] = mapped_column(String(255), comment="密码")
    wallet: Mapped[str] = mapped_column(String(100), comment="钱包地址")
    phone: Mapped[str] = mapped_column(String(11), unique=True, comment="电话号码")

