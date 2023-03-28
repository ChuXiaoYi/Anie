import json

from fastapi import APIRouter, Query, Depends, Body
from sqlalchemy import update
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.endpoints.auth import get_current_active_user
from app.models.post import Comment
from app.schema.comment import AddCommentReq
from app.schema.user import UserScheme

router = APIRouter()


@router.get('/list')
def get_comment_list(page: int = Query(..., title="页码"),
                     limit: int = Query(..., title="每页数量"),
                     db: Session = Depends(get_db),
                     current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            stmt = session.query(Comment)
            total = stmt.count()
            stmt = stmt.offset((page - 1) * limit).limit(limit)
            result = [item.to_dicts() for item in stmt]
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": {
            "total": total,
            "items": result
        }
    }


@router.get('/info')
def get_comment_details(comment_id: int = Query(..., title='文章id'), db: Session = Depends(get_db),
                        current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            comment = session.get(Comment, comment_id)
            if not comment:
                raise Exception("文章不存在")
            result = comment.to_dicts()

    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": {
            "items": result
        }
    }


@router.post('/add')
def add_comment(data: AddCommentReq = Body(),
                db: Session = Depends(get_db),
                current_user: UserScheme = Depends(get_current_active_user)):
    try:
        d = json.loads(data.json())
        with db as session:
            comment = Comment(**d, user_id=current_user.id)
            session.add(comment)
            session.commit()
            result = comment.to_dicts()
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": {
            "items": result
        }
    }


@router.put('/update')
def update_comment(comment_id: int = Query(..., title="文章id"),
                   data: AddCommentReq = Body(),
                   db: Session = Depends(get_db),
                   current_user: UserScheme = Depends(get_current_active_user)):
    try:
        d = json.loads(data.json())
        with db as session:
            with session.begin():
                comment = session.get(Comment, comment_id)
                if not comment:
                    raise Exception("文章不存在")
                stmt = update(Comment).where(Comment.id == comment_id).values(*d)
                session.execute(stmt)
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": {}
    }


@router.delete('/delete')
def delete_comment(comment_id: int = Query(..., title="文章id"),
                   db: Session = Depends(get_db),
                   current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            with session.begin():
                comment = session.get(Comment, comment_id)
                if not comment:
                    raise Exception("文章不存在")
                stmt = update(Comment).where(Comment.id == comment_id).values(status=0)
                session.execute(stmt)
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": {}
    }
