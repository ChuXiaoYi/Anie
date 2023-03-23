import uvicorn
from fastapi import FastAPI, Request, Response
from starlette.middleware.sessions import SessionMiddleware

from app.api.api import router
from app.config import config
from app.db.session import SessionLocal

app = FastAPI()
app.include_router(router)

app.add_middleware(SessionMiddleware, secret_key=config.SECRET_KEY, session_cookie="anie",
                   max_age=None)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


if __name__ == '__main__':
    uvicorn.run('main:app', port=8000, reload=True)
