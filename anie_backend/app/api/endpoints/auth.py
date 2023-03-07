from fastapi import APIRouter

router = APIRouter()


@router.post('/login')
def login():
    pass


@router.get('/logout')
def logout():
    pass


@router.post('/register')
def register():
    pass
