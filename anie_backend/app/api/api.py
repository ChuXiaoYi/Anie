from fastapi import APIRouter

from app.api.endpoints import user
from app.api.endpoints import nft
from app.api.endpoints import animal
from app.api.endpoints import auth

router = APIRouter()

router.include_router(user.router, tags=['登陆认证'])
router.include_router(nft.router, tags=['NFT'])
router.include_router(animal.router, prefix='/animal', tags=['宠物信息'])
router.include_router(auth.router, tags=['权限管理'])
