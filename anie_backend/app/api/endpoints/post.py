import json

from fastapi import APIRouter, Query, Depends, Body
from sqlalchemy import update
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.endpoints.auth import get_current_active_user
from app.models.post import Post
from app.schema.post import AddPostReq
from app.schema.user import UserScheme

router = APIRouter()


@router.get('/list')
def get_post_list(page: int = Query(..., title="页码"),
                  limit: int = Query(..., title="每页数量"),
                  db: Session = Depends(get_db),
                  current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            stmt = session.query(Post)
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
def get_post_details(post_id: int = Query(..., title='文章id'), db: Session = Depends(get_db),
                     current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            post = session.get(Post, post_id)
            if not post:
                raise Exception("文章不存在")
            result = post.to_dicts()

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
def add_post(data: AddPostReq = Body(),
             db: Session = Depends(get_db),
             current_user: UserScheme = Depends(get_current_active_user)):
    try:
        d = json.loads(data.json())
        with db as session:
            post = Post(**d, user_id=current_user.id)
            session.add(post)
            session.commit()
            result = post.to_dicts()
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
def update_post(post_id: int = Query(..., title="文章id"),
                data: AddPostReq = Body(),
                db: Session = Depends(get_db),
                current_user: UserScheme = Depends(get_current_active_user)):
    try:
        d = json.loads(data.json())
        with db as session:
            with session.begin():
                post = session.get(Post, post_id)
                if not post:
                    raise Exception("文章不存在")
                stmt = update(Post).where(Post.id == post_id).values(*d)
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
def delete_post(post_id: int = Query(..., title="文章id"),
                db: Session = Depends(get_db),
                current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            with session.begin():
                post = session.get(Post, post_id)
                if not post:
                    raise Exception("文章不存在")
                stmt = update(Post).where(Post.id == post_id).values(status=0)
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
