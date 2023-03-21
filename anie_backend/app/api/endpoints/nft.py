import random

from fastapi import APIRouter

from app.utils.make_nft import creature

router = APIRouter()


@router.get('/token_uri')
def get_token_uri():
    nonce = random.randint(0, 10)
    uri = creature(nonce)
    return {
        "code": 0,
        "msg": "success",
        "data": {
            "uri": uri
        }
    }

