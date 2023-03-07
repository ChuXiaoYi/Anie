from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('', pool_pre_ping=True)
Session = sessionmaker(bind=engine, autoflush=False, autocommit=True)
