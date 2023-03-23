from fastapi import APIRouter, Query, Depends, Request
from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session

from app.api.deps import get_db
from app.api.endpoints.auth import get_password_hash
from app.contract.wallet import create_wallet_address
from app.models.user import User
from app.schema.user import RegisterReq

router = APIRouter()


@router.post('/register', description="注册")
def register(request: Request, data: RegisterReq, db: Session = Depends(get_db)):
    try:
        if data.code != request.session[data.phone]:
            return {
                "code": -1,
                "msg": "注册失败,验证码错误",
                "details": {}
            }
        address, private_key = create_wallet_address()
        with db as session:
            user = User(phone=data.phone, password=get_password_hash(data.password1), username=data.username, wallet=address)
            session.add(user)
            session.commit()
    except IntegrityError as e:
        return {
            "code": -1,
            "msg": "注册失败,该手机号已注册",
            "details": {}
        }
    except Exception as e:
        return {
            "code": -1,
            "msg": "注册失败,请重试",
            "details": e.args[0] if e.args else {}
        }
    return {
        "code": 0,
        "msg": "用户创建成功，请保存私钥，私钥不可泄露",
        "details": {
            "address": address,
            "private_key": private_key
        }
    }


@router.get('/get_validata_code', description="获取验证码")
def get_validata_code(request: Request, phone: str = Query(..., title="手机号")):
    try:
        request.session[phone] = '123456'
    except Exception as e:
        return {
            "code": 0,
            "msg": "获取验证码失败,请重试",
            "details": e.args[0] if e.args else {}
        }
    return {
        "code": 0,
        "msg": "success",
        "details": {
            "code": "123456"
        }
    }
