#database.py defines the table

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, scoped_session

# Define base class
class Base(DeclarativeBase):
    pass

# Create engine and connect to SQLite database 'echo=True' see SQL queries
import os
db_path = os.environ.get('DATABASE_URL', 'sqlite:///blog.db')
engine = create_engine('sqlite:///blog.db', echo=True)

"""
scoped_session creates a safe thread 
db_session creates a ready session instance import to app.py
innit_db efficient to create tables explicitly when starting app rather than imoport
"""
SessionLocal = scoped_session(sessionmaker(bind=engine))
db_session = SessionLocal

def init_db():
    import model

    # Create tables based on model metadata
    Base.metadata.create_all(engine)