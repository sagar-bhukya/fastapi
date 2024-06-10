from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from schemas import response_Blog,BlogCreate
from database import get_db
from models import Blog,User
from sqlalchemy.orm import Session
from repository import blog
from oauth2 import get_current_user

router=APIRouter(
    prefix="/blog",
    tags=["blogs"]
)

@router.get('/',response_model=List[response_Blog])# here you get with field from the all within List
def get_all(db:Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    # get_all=db.query(Blog).all()   #move to the repository file
    return blog.get_all(db)


@router.post('/',status_code=status.HTTP_201_CREATED)
def create_blog(response_shecma: BlogCreate, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
    return blog.create(response_shecma,db)


#this is for get only one blog item
@router.get('/{id}',response_model=response_Blog)
def show_item(id:int,db:Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    return blog.show_blog(id,db)

#for delete a blog with id
@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session=Depends(get_db),current_user:User=Depends(get_current_user)):
    # del_blog=db.query(Blog).filter(Blog.id==id).first()
    # if not del_blog:
    #     raise HTTPException(status_code=404,detail="Blog is not found") 
    # db.delete(del_blog)
    # db.commit()
    # return {"message": f"with {id} of the data has deleted"}

    return blog.delete_blog(id,db)


#this is for update a blog
@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db),current_user:User=Depends(get_current_user)):
#     blog_query = db.query(Blog).filter(Blog.id == id)
#     blog = blog_query.first()
#     if blog is None:
#         raise HTTPException(status_code=404, detail="Blog not found")
    
#     blog_query.update(request.dict())
#     db.commit()
    
#     return "done"
        return blog.update_blog(id,request,db)

