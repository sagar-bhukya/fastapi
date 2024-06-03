from sqlalchemy.orm import Session
from models import Item,Patient
from fastapi import HTTPException
from typing import List


def get_all_items(db: Session) -> List[Item]:
    return db.query(Item).all()

def create_an_item(db: Session, item: Item) -> Item:
    existing_item = db.query(Item).filter(Item.id == item.id).first()
    if existing_item is not None:
        raise HTTPException(status_code=400, detail="Item with this ID already exists")
    db_item = Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_item_by_id(db: Session, item_id: int) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

def update_an_item(db: Session, item_id: int, updated_item: Item) -> Item:
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    item.name = updated_item.name
    item.description = updated_item.description
    item.on_offer = updated_item.on_offer
    item.price = updated_item.price
    db.commit()
    db.refresh(item)
    return item

def delete_an_item(db: Session, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item with id {item_id} deleted successfully"}

from typing import Dict


'''{
    "patient_id": "123456",
    "name": {
      "first_name": "John",
      "last_name": "Doe"
    },
    "age": 35,
    "gender": "male",
    "contact": {
      "phone": "123-456-7890",
      "email": "john.doe@example.com"
    },
    "address": {
      "street": "123 Main St",
      "city": "Anytown",
      "state": "CA",
      "zipcode": "12345"
    },
    "medical_history": {
      "conditions": [
        "Hypertension",
        "Diabetes"
      ],
      "medications": [
        "Lisinopril",
        "Metformin"
      ],
      "allergies": [
        "Penicillin"
      ]
    }
  }'''
#for JSon data
# def create_patient(db: Session, patient_data: Dict) -> Patient:
#     name_data = patient_data.pop('name')
#     contact_data = patient_data.pop('contact')
#     address_data = patient_data.pop('address')
#     medical_history_data = patient_data.pop('medical_history')

#     patient = Patient(
#         name=name_data,
#         contact=contact_data,
#         address=address_data,
#         medical_history=medical_history_data,
#         **patient_data
#     )
#     db.add(patient)
#     db.commit()
#     db.refresh(patient)
#     return patient

def create_patient(db: Session, patient_data: Dict) -> Patient:
    try:

        patient = Patient(**patient_data)#Patient(**patient_data) is a shorthand way to pass all the dictionary key-value pairs as keyword arguments to the Patient constructor.
        print("patient_data\n",patient)
        print("----------")
        db.add(patient)
        db.commit()
        db.refresh(patient)
        print("---------------------\n",patient)
        return patient
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating patient: {e}")

def get_all_patient(db:Session)->List[Patient]:
    get_all_patient=db.query(Patient).all()
    print("get all patient data\n -------",get_all_patient)
    return get_all_patient

def get_patient_by_id(db:Session,patient_id:str)->Patient:
    get_patient_id=db.query(Patient).filter(Patient.patient_id==patient_id).first()
    print("patient_id\n-----",get_patient_by_id)
    return get_patient_id


#update an patient with patient id
def update_patient(db:Session,patien_id:int,patient_data:Patient)->Patient:
    patient=db.query(Patient).filter(Patient.patient_id==patien_id).first()
    print(patient,"***************")
    print("----------")
    if not patient:
        raise HTTPException(status_code=400,detail="Patient Not Found")
    print("patient data -----\n",patient_data)
    update_data=patient_data.dict()
    print("dict patient data\n-----",update_data)#This is useful for iterating over the attributes and their values.
    for key,value in update_data.items():
        print("key------\n",key,"\n","value====\n",value)
        if value is not None:
            print("patient-----\n",patient)
            print("data update---\n",setattr(patient, key, value))#this will helps 
    db.commit()
    db.refresh(patient)
    return patient

#delete patient with patient_id
def delete_patient(db:Session,patient_id=str):
    patient_delete=db.query(Patient).filter(Patient.patient_id==patient_id).all()

    if patient_delete is None:
        raise HTTPException(status_code=400,detail="patient_id not found")
    for patient in patient_delete:
        db.delete(patient)
    db.commit()
    return {"message":f"the patient is deleted with {patient_id} patient id"}




