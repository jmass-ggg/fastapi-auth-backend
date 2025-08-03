from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:Kanye%4012@localhost:5432/mydb"
engine=create_engine(DATABASE_URL,pool_pre_ping=True)
Base=declarative_base()
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()