import json
import traceback
from datetime import timedelta, datetime

from fastapi import APIRouter, Request, Depends, HTTPException, Response, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pymysql import IntegrityError
from sqlalchemy.orm import Session
from starlette import status

from app.api.deps import get_db
from app.config import config
from app.contract.wallet import create_wallet_address
from app.models.user import User
from app.schema.user import UserScheme, LoginReq, RegisterReq

router = APIRouter()

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = config.SECRET_KEY
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


def get_user(db: Session, phone: str):
    with db as session:
        user = session.query(User).filter(User.phone == phone).first()
    return user


def authenticate_user(db: Session, phone: str, password: str):
    user = get_user(db, phone)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return UserScheme(**user.to_dicts())


def authenticate_user_from_code(db: Session, phone: str, code: str, origin_code: str):
    user = get_user(db, phone)
    if not user:
        return False
    if not code == origin_code:
        return False
    return UserScheme(**user.to_dicts())


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        user: UserScheme = UserScheme(**json.loads(payload.get("sub")))
        print(user)
        if user.phone is None:
            raise credentials_exception
    except Exception as e:
        print(traceback.format_exc())
        raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(db, phone=user.phone)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
        current_user: User = Depends(get_current_user)
):
    if not current_user.status:
        raise HTTPException(status_code=400, detail="Inactive user")
    return UserScheme(**current_user.to_dicts())


@router.post("/token")
async def login_for_access_token(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(get_db)
):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.json()}, expires_delta=access_token_expires
    )

    return {
        "code": 0,
        "msg": "success",
        "details": {"access_token": access_token, "token_type": "bearer"}
    }


@router.post('/login', description="登录 - 通过验证码")
def login(request: Request, data: LoginReq, db: Session = Depends(get_db)):
    try:
        origin_code = request.session.get(data.phone)
        user = authenticate_user_from_code(db, data.phone, data.code, origin_code)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": user.dict()}, expires_delta=access_token_expires
        )
    except Exception as e:
        return {
            "code": 0,
            "msg": "登录失败,请重试",
            "details": e.args[0] if e.args else {}
        }
    return {
        "code": 0,
        "msg": "success",
        "details": {"access_token": access_token, "token_type": "bearer"}
    }


@router.post("/current_user")
async def read_users_me(current_user: UserScheme = Depends(get_current_active_user)):
    return {
            "code": 0,
            "msg": "success",
            "details": current_user
        }


@router.post('/logout', description="退出登录")
def logout(response: Response, token: str = Depends(oauth2_scheme)):
    try:
        response.delete_cookie("Authorization")
    except Exception as e:
        return {
            "code": 0,
            "msg": "退出登录失败,请重试",
            "details": e.args[0] if e.args else {}
        }
    return {
        "code": 0,
        "msg": "success",
        "details": {}
    }


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
