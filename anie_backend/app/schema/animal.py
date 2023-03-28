from typing import List

from fastapi import Body
from pydantic import BaseModel

from app.constant import Gender, AnimalCategoryEnum, DogSubCategoryEnum


class AddPetReq(BaseModel):
    name: str = Body(..., title="昵称")
    gender: Gender = Body(..., title="性别")
    category: AnimalCategoryEnum = Body(..., title="动物种类")
    sub_category: DogSubCategoryEnum = Body(..., title="品种子类")
    images: List[str] = Body(..., title="宠物图片: 正脸 和 鼻部")


class UpdatePetReq(BaseModel):
    name: str = Body(..., title="昵称")
    gender: Gender = Body(..., title="性别")
    category: AnimalCategoryEnum = Body(..., title="动物种类")
    sub_category: DogSubCategoryEnum = Body(..., title="品种子类")
    images: List[str] = Body(..., title="宠物图片: 正脸 和 鼻部")
