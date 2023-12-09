from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:pedro20761867@localhost/PIX-AI'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        #get all the data from db and return
        yield db
    finally:
        db.close()

def dbSession(decorated_function):
    def wrapper(*args, **kwargs):
        with next(get_db()) as db:
            return decorated_function(*args, db=db, **kwargs)
    return wrapper