from database import Base
from sqlalchemy import Integer,String,Boolean,Column,Text,JSON

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"
    


class Patient(Base):
    __tablename__ = 'patients'

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(String, unique=True, index=True)
    name = Column(JSON,nullable=True)
    age = Column(Integer,nullable=True)
    gender = Column(String, nullable=True)
    contact = Column(JSON,nullable=True)
    address = Column(JSON,nullable=True)
    medical_history = Column(JSON,nullable=True)