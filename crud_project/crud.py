from sqlalchemy.orm import Session
from models import Item
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
