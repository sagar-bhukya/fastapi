from database import Base
from sqlalchemy import Column,Integer,String


class Blog(Base):
    __tablename__="Blogs"
    id= Column(Integer,primary_key=True)#indexed for faster queries
    title=Column(String)
    body=Column(String)
