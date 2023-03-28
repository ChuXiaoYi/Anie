from typing import List

from sqlalchemy import String, SmallInteger, Integer, JSON
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class Animal(Base):
    __tablename__ = "animal"

    name: Mapped[str] = mapped_column(String(255), comment="昵称")
    gender: Mapped[int] = mapped_column(SmallInteger, comment="性别")
    category: Mapped[int] = mapped_column(SmallInteger, comment="动物种类")
    sub_category: Mapped[int] = mapped_column(SmallInteger, comment="品种子类")
    images: Mapped[List[str]] = mapped_column(JSON, default=[], comment="宠物图片: 正脸 和 鼻部")

    user_id: Mapped[int] = mapped_column(Integer, comment="用户id")


class AnimalCategory(Base):
    __tablename__ = "animal_category"

    name: Mapped[str] = mapped_column(String(100), comment="名称")
    parent_id: Mapped[int] = mapped_column(Integer, comment="父级id", default=0)
