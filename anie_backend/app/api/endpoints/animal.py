import json
import traceback

from fastapi import APIRouter, Depends, Body, Query
from sqlalchemy import update
from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.endpoints.auth import get_current_active_user
from app.models.animal import AnimalCategory, Animal
from app.schema.animal import AddPetReq, UpdatePetReq
from app.schema.user import UserScheme

router = APIRouter()


@router.get('/list')
def get_ani_list(page: int = Query(..., title="页码"),
                 limit: int = Query(..., title="每页数量"),
                 db: Session = Depends(get_db),
                 current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            stmt = session.query(Animal).filter(Animal.user_id == current_user.id)
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
def get_ani_details(aid: int = Query(..., title="id"),
                    db: Session = Depends(get_db),
                    current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            stmt = session.query(Animal).filter(Animal.id == aid, Animal.user_id == current_user.id).first()
            if not stmt:
                raise Exception("宠物不存在")
            result = stmt.to_dicts()
    except Exception as e:
        return {
            "code": -1,
            "msg": str(e),
            "data": {}
        }
    return {
        "code": 0,
        "msg": "success",
        "data": result
    }


@router.post('/add')
def add_ani(data: AddPetReq = Body(...), db: Session = Depends(get_db),
            current_user: UserScheme = Depends(get_current_active_user)):
    try:
        with db as session:
            with session.begin():
                d = json.loads(data.json())
                session.add(Animal(**d, user_id=current_user.id))
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


@router.put('/update')
def update_ani(aid: int = Query(..., title='id'),
               data: UpdatePetReq = Body(...),
               db: Session = Depends(get_db),
               current_user: UserScheme = Depends(get_current_active_user)):
    try:
        d = json.loads(data.json())
        with db as session:
            with session.begin():
                animal = session.get(Animal, aid)
                if not animal:
                    raise Exception("宠物不存在")
                stmt = (update(Animal).where(Animal.id == aid).values(**d))
                session.execute(stmt)

    except Exception as e:
        print(traceback.format_exc())
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
def delete_ani(aid: int = Query(..., title='id'),
               db: Session = Depends(get_db)):
    try:
        with db as session:
            with session.begin():
                stmt = update(Animal).where(Animal.id == aid).values(status=0)
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


@router.get('/get_category')
def get_category(db: Session = Depends(get_db)):
    try:
        with db as session:
            stmt = session.query(AnimalCategory).all()
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
            "category": result
        }
    }
