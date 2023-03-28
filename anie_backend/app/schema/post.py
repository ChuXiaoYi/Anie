from typing import List

from fastapi import Body
from pydantic import BaseModel

from app.constant import AnimalCategoryEnum


class AddPostReq(BaseModel):
    title: str = Body(..., title="标题")
    medias: List[dict] = Body(..., title="媒体")
    content: str = Body(..., title="内容")
    category: AnimalCategoryEnum = Body(..., title="分类")
    tags: List[str] = Body(..., title="标签")


class UpdatePostReq(AddPostReq):
    pass
