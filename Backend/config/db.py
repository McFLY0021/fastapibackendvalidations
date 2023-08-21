from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
"""Modifica esta talla pa que lo pruebes"""

SQLALCHEMY_DATABASE_URL = 'mysql+cymysql://root:@localhost:3306/db_prueba'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()