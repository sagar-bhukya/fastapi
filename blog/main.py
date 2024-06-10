from fastapi import FastAPI,Depends,status,HTTPException
from pydantic import BaseModel
from typing import List
from models import Base,Blog,User
from database import engine,SessionLocal,get_db
from schemas import BlogCreate,response_Blog,schema_user,showUser
from sqlalchemy.orm import Session
from hashing import Hash

from passlib.context import CryptContext #for password hashing purpose
from routers import blog,user,authentication


app=FastAPI()
Base.metadata.create_all(bind=engine)

#register here for the routers
app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)
# def get_db():
#     db=SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()




#for creating the blog
# @app.post('/bog',response_model=BlogCreate,status_code=201)
# @app.post('/blog',status_code=status.HTTP_201_CREATED,tags=["blogs"])
# def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
#     db_blog = Blog(title=blog.title, body=blog.body,user_id=1)#this is manually written 
#     # db_blog=Blog(**blog.dict())# dynamically
#     db.add(db_blog)
#     db.commit()
#     db.refresh(db_blog)
#     return db_blog



#this is for get all the data
# @app.get('/blogs',response_model=List[response_Blog],tags=["blogs"])# here you get with field from the all within List
# def get_all(db:Session = Depends(get_db)):
#     get_all=db.query(Blog).all()
#     return get_all



#this is for get only one blog item
# @app.get('/blog_with_id/{id}',response_model=response_Blog,tags=["blogs"])
# def show_otem(id:int,db:Session=Depends(get_db)):
#     get_blog=db.query(Blog).filter(Blog.id==id).first()
#     #if item not found something should display
#     if not get_blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"item with the {id} is not found")
#     return get_blog



#for delete a blog with id
# @app.delete('/blog_delete/{id}',status_code=status.HTTP_204_NO_CONTENT,tags=["blogs"])
# def delete_blog(id:int, db: Session=Depends(get_db)):
#     del_blog=db.query(Blog).filter(Blog.id==id).first()
#     if not del_blog:
#         raise HTTPException(status_code=404,detail="Blog is not found") 
#     db.delete(del_blog)
#     db.commit()
#     return {"message": f"with {id} of the data has deleted"}



#this is for update a blog
# @app.put('/update_Blog/{id}', status_code=status.HTTP_202_ACCEPTED,tags=["blogs"])
# def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db)):
#     blog_query = db.query(Blog).filter(Blog.id == id)
#     blog = blog_query.first()
#     if blog is None:
#         raise HTTPException(status_code=404, detail="Blog not found")
    
#     blog_query.update(request.dict())
#     db.commit()
    
#     return "done"



# #psw_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")


# @app.post('/user',response_model=showUser,tags=["users"]) # this will show only name and email
# def create_user(request:schema_user,db: Session=Depends(get_db)):
#     # user_create=User(**request.dict())# for dynamic value insert


#     # hashed_pswd=psw_cxt.hash(request.password) # for this we have created another class 
#     hashed_pswd_class=Hash.dcrypt(request.password)
#     user_data=request.dict()
#     # user_data["password"]=hashed_pswd # for manually insert value for password dict

#     user_data["password"]=hashed_pswd_class
#     user_create=User(**user_data)
#     db.add(user_create)
#     db.commit()
#     db.refresh(user_create)
#     return user_create




# #get id of user
# @app.get('/user/{id}',response_model=showUser,tags=["users"])
# def get_user_id(id:int,db:Session=Depends(get_db)):
#     get_user=db.query(User).filter(User.id==id).first()
#     if not get_user:
#         raise HTTPException(status_code=404,detail=f"user not found with {id} id")
#     return get_user




# @app.delete('/user/{id}',tags=["users"])
# def delete_user(id:int,db:Session=Depends(get_db)):
#     delete_us=db.query(User).filter(User.id==id).first()
#     db.delete(delete_us)
#     db.commit()
#     return "delete susccess"

