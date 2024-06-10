from pydantic import BaseModel
from typing import List,Optional

class BlogCreate(BaseModel):
    title: str
    body: str
    # user_id: int
#create user schema model
class schema_user(BaseModel):

    name:str
    email:str
    password:str

#for getting only user in the sense name and email only
class showUser(BaseModel):
    name:str
    email:str
    blogs: List[BlogCreate]=[]
    class Config:
        orm_mode = True

class response_Blog(BaseModel):
    title:str
    body:str
    creator:showUser
    class Config():# this is because we are writing orm query so thats why we use 
        orm_mode=True


class Login(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    email:Optional[str] =None