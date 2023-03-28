from typing import List

from sqlalchemy import String, JSON, Text, Integer
from sqlalchemy.orm import mapped_column, Mapped

from app.constant import AnimalCategoryEnum
from app.models.base import Base


class Post(Base):
    __tablename__ = "post"

    title: Mapped[str] = mapped_column(String(255), comment="标题")
    medias: Mapped[List[dict]] = mapped_column(JSON, default=[], comment="媒体")
    content: Mapped[str] = mapped_column(Text, comment="内容")
    star: Mapped[int] = mapped_column(Integer, comment="点赞数", default=0)
    collect: Mapped[int] = mapped_column(Integer, comment="收藏数", default=0)
    category: Mapped[AnimalCategoryEnum] = mapped_column(Integer, comment="分类")
    tags: Mapped[List[str]] = mapped_column(JSON, default=[], comment="标签")

    user_id: Mapped[int] = mapped_column(Integer, comment="用户id")


class Comment(Base):
    __tablename__ = "comment"

    content: Mapped[str] = mapped_column(Text, comment="内容")
    star: Mapped[int] = mapped_column(Integer, comment="点赞数", default=0)

    user_id: Mapped[int] = mapped_column(Integer, comment="用户id")
    post_id: Mapped[int] = mapped_column(Integer, comment="帖子id")
    parent_id: Mapped[int] = mapped_column(Integer, comment="父级id", default=0)
