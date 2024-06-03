from typing import List,Optional
from pydantic import BaseModel
from pydantic.dataclasses import dataclass

@dataclass
class Address(BaseModel):
    street: Optional[str]=''
    city: Optional[str]=None
    state: Optional[str]=None
    zipcode: Optional[str]=None
@dataclass
class Name(BaseModel):
    first_name: Optional[str]=None
    last_name: Optional[str]=None
@dataclass
class Contact(BaseModel):
    phone: Optional[str]=None
    email: Optional[str]=None
@dataclass
class MedicalHistory(BaseModel):
    conditions: Optional[List[str]]
    medications: Optional[List[str]]
    allergies: Optional[List[str]]
@dataclass
class Patient_response(BaseModel):
    patient_id: Optional[str]=None
    name: Optional[Name]=None
    age: Optional[int]=None
    gender: Optional[str] = None
    contact: Optional[Contact]=None
    address: Optional[Address]=None
    medical_history: Optional[MedicalHistory]=None
