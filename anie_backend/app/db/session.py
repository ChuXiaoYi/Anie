from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:123456@localhost/anie', pool_pre_ping=True, echo=True, future=True)
SessionLocal = sessionmaker(bind=engine, autoflush=False)
