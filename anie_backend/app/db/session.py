from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config import config

engine = create_engine(
    f'mysql+pymysql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}',
    pool_pre_ping=True, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
