from database import Base
from sqlalchemy import Integer,String,Boolean,Column,Text

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Integer)
    on_offer = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Item name={self.name} price={self.price}>"