from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from models import Blog
from database import get_db
from schemas import BlogCreate



def get_all(db:Session = Depends(get_db)):
    return db.query(Blog).all()


def create(blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = Blog(title=blog.title, body=blog.body,user_id=1)#this is manually written 
    # db_blog=Blog(**blog.dict())# dynamically
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def show_blog(id:int,db:Session=Depends(get_db)):
    get_blog=db.query(Blog).filter(Blog.id==id).first()
    #if item not found something should display
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"item with the {id} is not found")
    return get_blog


def delete_blog(id:int, db: Session=Depends(get_db)):
    del_blog=db.query(Blog).filter(Blog.id==id).first()
    if not del_blog:
        raise HTTPException(status_code=404,detail=f"Blog {id} is not found") 
    db.delete(del_blog)
    db.commit()
    return {"message": f"with {id} of the data has deleted"}


def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog_query.update(request.dict())
    db.commit()
    
    return "done"