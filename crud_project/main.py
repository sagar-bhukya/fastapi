# from fastapi import FastAPI,Depends,status,HTTPException
# from pydantic import BaseModel
# from typing import List
# from database import SessionLocal
# import models
# from sqlalchemy.orm import Session



# app=FastAPI()



# # @app.get('/end-point')
# # async def get():
# #     return {"message":"Hi sagar"}


# # @app.get('/get_name/{name}')
# # async def getname(name:str):
# #     return {"yourname": f"{name}"}

# # @app.put('/item/{item_id}')
# # def update_item(item_id:int,item:Item):
# #     return {
# #         "name":item.name,
# #         "description":item.description,
# #         "price":item.price,
# #         "on_offer":item.on_offer
# #     }



# class Item(BaseModel):
#     id:int
#     name:str
#     description:str
#     price:int
#     on_offer:bool

#     class Config:
#         orm_mode=True

# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.get('/items',response_model=List[Item],status_code=200)
# def get_all_items( db: Session = Depends(get_db)):
#     items=db.query(models.Item).all()
#     return items        
    

# # @app.post('/items/',response_model=Item,status_code=status.HTTP_201_CREATED)
# # def get_an_item(item:Item,db:Session=Depends(get_db)):
# #     db_item=models.Item(**item.dict())
# #     db.add(db_item)
# #     db.commit()
# #     db.refresh(db_item)
# #     return db_item
# @app.post('/items/', status_code=status.HTTP_201_CREATED)
# def create_an_item(item: Item, db: Session = Depends(get_db)):
#     existing_item=db.query(models.Item).filter(models.Item.id==item.id).first()
#     if existing_item is not None:
#         raise HTTPException(status_code=400,detail="Item with this ID already Exists")
#     db_item = models.Item(**item.dict())
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return {"message": f"Item created successfully with id {db_item.id}", "item": db_item}

# @app.get('/items/{item_id}',status_code=200,response_model=Item)
# def post_data(item_id:int,db:Session=Depends(get_db)):
#     item =db.query(models.Item).filter(models.Item.id==item_id).first()
#     if item is None:
#         raise HTTPException(status_code=404,detail="Item not found")
#     return item


# @app.put('/items/{item_id}',response_model=Item,status_code=200)
# def update_an_item(item_id:int,updated_item:Item,db: Session=Depends(get_db)):
#     item=db.query(models.Item).filter(models.Item.id==item_id).first()
#     if item is None:
#         raise HTTPException(status_code=404,detail="Item not Found")
#     item.name=updated_item.name
#     item.description=updated_item.description
#     item.on_offer=updated_item.on_offer
#     item.price=updated_item.price
#     db.commit()
#     db.refresh(item)
#     return item

# @app.delete('/items/{item_id}',status_code=status.HTTP_201_CREATED)
# def delete_an_item(item_id:int,db:Session=Depends(get_db)):
#     item=db.query(models.Item).filter(models.Item.id==item_id).first()
#     if item is None:
#         raise HTTPException(status_code=404,detail="item not found")
#     db.delete(item)
#     db.commit()
#     return {"message": f"Item with id {item_id} deleted successfully"}



from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from sqlalchemy.orm import Session

import crud

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str
    price: int
    on_offer: bool

    class Config:
        orm_mode = True

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get('/items', response_model=List[Item], status_code=200)
def get_all_items(db: Session = Depends(get_db)):
    return crud.get_all_items(db)

@app.post('/items/', status_code=status.HTTP_201_CREATED)
def create_an_item(item: Item, db: Session = Depends(get_db)):
    db_item = crud.create_an_item(db, item)
    return {"message": f"Item created successfully with id {db_item.id}", "item": db_item}

@app.get('/items/{item_id}', status_code=200, response_model=Item)
def get_item_by_id(item_id: int, db: Session = Depends(get_db)):
    return crud.get_item_by_id(db, item_id)

@app.put('/items/{item_id}', response_model=Item, status_code=200)
def update_an_item(item_id: int, updated_item: Item, db: Session = Depends(get_db)):
    return crud.update_an_item(db, item_id, updated_item)

@app.delete('/items/{item_id}', status_code=status.HTTP_201_CREATED)
def delete_an_item(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_an_item(db, item_id)




