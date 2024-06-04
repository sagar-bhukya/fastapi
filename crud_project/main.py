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



#Data Validation: Ensures incoming data matches the expected types and structure.
#Data Serialization: Converts complex data types (like database models) into JSON format for HTTP responses

from fastapi import FastAPI, Depends, status, HTTPException
from pydantic import BaseModel
from typing import List
from database import SessionLocal
from sqlalchemy.orm import Session
from models import Patient
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

# class Address(BaseModel):
#     street: str
#     city: str
#     state: str
#     zipcode: str

# class Name(BaseModel):
#     first_name: str
#     last_name: str

# class Contact(BaseModel):
#     phone: str
#     email: str

# class MedicalHistory(BaseModel):
#     conditions: List[str]
#     medications: List[str]
#     allergies: List[str]

# class Patient_response(BaseModel):
#     patient_id: str
#     name: Name
#     age: int
#     gender: str
#     contact: Contact
#     address: Address
#     medical_history: MedicalHistory
from Schemas import Patient_response
@app.post('/patients/', status_code=status.HTTP_201_CREATED, response_model=Patient_response)
def create_patient(patient_data: Patient_response, db: Session = Depends(get_db)):
    patient_dict = patient_data.dict()
    print("converting into dict\n",patient_dict)
    patient = crud.create_patient(db, patient_dict)
    return patient

#for getting all the data of the patient
@app.get('/patients/',status_code=200,response_model=List[Patient_response])
def get_all_patient(db:Session=Depends(get_db)):
    return crud.get_all_patient(db)

#for getting the  patient data with patient id
@app.get('/patients/{patient_id}', response_model=Patient_response, status_code=200)
def read_patient(patient_id: str, db: Session = Depends(get_db)):
    patient = crud.get_patient_by_id(db, patient_id)
    if patient is None:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient

#for update the patient
@app.put('/patients/{patient_id}',response_model=Patient_response,status_code=200)
def update_patient(patient_id: str,update_body:Patient_response,db:Session=Depends(get_db)):
    return crud.update_patient(db,patient_id,update_body)

#for delete the patient data
@app.delete('/patient/{patient_id}',status_code=201)
def patient_delete(patient_id:str,db:Session=Depends(get_db)):
    return crud.delete_patient(db,patient_id)



