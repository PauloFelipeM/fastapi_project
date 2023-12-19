from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine=create_engine("mysql+mysqlconnector://root:1NfHJ9WKX2YIZ@database:3306/fastapi", echo=True)

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

Base.query = db_session.query_property()

def init_db():
    import models
    Base.metadata.create_all(bind=engine)