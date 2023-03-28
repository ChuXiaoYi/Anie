from fastapi import APIRouter

from app.api.endpoints import user
from app.api.endpoints import nft
from app.api.endpoints import animal
from app.api.endpoints import auth
from app.api.endpoints import post
from app.api.endpoints import comment

router = APIRouter()

router.include_router(user.router, tags=['登陆认证'])
router.include_router(nft.router, tags=['NFT'])
router.include_router(animal.router, prefix='/animal', tags=['宠物信息'])
router.include_router(auth.router, tags=['权限管理'])
router.include_router(post.router, prefix='/post', tags=['文章管理'])
router.include_router(comment.router, prefix='/comment', tags=['评论管理'])
