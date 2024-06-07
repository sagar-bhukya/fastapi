from fastapi import FastAPI,Depends,status,HTTPException
from pydantic import BaseModel
from models import Base,Blog
from database import engine,SessionLocal
from schemas import BlogCreate
from sqlalchemy.orm import Session

app=FastAPI()
Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

#for creating the blog
# @app.post('/bog',response_model=BlogCreate,status_code=201)
@app.post('/bog',response_model=BlogCreate,status_code=status.HTTP_201_CREATED)
def create_blog(blog: BlogCreate, db: Session = Depends(get_db)):
    db_blog = Blog(title=blog.title, body=blog.body)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

#this is for get all the data
@app.get('/blogs')
def get_all(db:Session = Depends(get_db)):
    get_all=db.query(Blog).all()
    return get_all

#this is for get only one blog item
@app.get('/blog_with_id/{id}')
def show_otem(id:int,db:Session=Depends(get_db)):
    get_blog=db.query(Blog).filter(Blog.id==id).first()
    #if item not found something should display
    if not get_blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"item with the {id} is not found")
    return get_blog

#for delete a blog with id
@app.delete('/blog_delete/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id:int, db: Session=Depends(get_db)):
    del_blog=db.query(Blog).filter(Blog.id==id).first()
    if not del_blog:
        raise HTTPException(status_code=404,detail="Blog is not found") 
    db.delete(del_blog)
    db.commit()
    return {"message": f"with {id} of the data has deleted"}

#this is for update a blog
@app.put('/update_Blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: BlogCreate, db: Session = Depends(get_db)):
    blog_query = db.query(Blog).filter(Blog.id == id)
    blog = blog_query.first()
    if blog is None:
        raise HTTPException(status_code=404, detail="Blog not found")
    
    blog_query.update(request.dict())
    db.commit()
    
    return "done"