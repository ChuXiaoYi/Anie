from fastapi import Body
from pydantic import BaseModel, validator


class RegisterReq(BaseModel):
    username: str = Body(..., title="用户名")
    phone: str = Body(..., title="手机号")
    code: str = Body(..., title="验证码")
    password1: str = Body(..., title="密码1")
    password2: str = Body(..., title="密码2")

    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        if 'password1' in values and v != values['password1']:
            raise ValueError('密码不一致')
        return v


class LoginReq(BaseModel):
    """
    登录请求 - 验证码登陆
    """
    phone: str = Body(..., title="用户名")
    code: str = Body(..., title="验证码")


class UserScheme(BaseModel):
    id: int
    username: str
    phone: str
    status: int
