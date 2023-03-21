from fastapi import APIRouter

router = APIRouter()


@router.post('/add')
def create_pet():
    pass
