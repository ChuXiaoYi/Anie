from fastapi import Body
from pydantic import BaseModel


class AddCommentReq(BaseModel):
    content: str = Body(..., title="评论内容")
    post_id: int = Body(..., title="文章id")
    parent_id: int = Body(0, title="父级id")
