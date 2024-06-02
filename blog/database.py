from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Db_url='sqlite:/// ./blog.db'
engine= create_engine(Db_url,connect_args={"check_same_thread":False})

SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False,)
Base=declarative_base()