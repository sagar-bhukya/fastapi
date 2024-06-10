from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from models import Blog,User
from database import get_db
from schemas import BlogCreate,schema_user
from hashing import Hash



def create_user(request:schema_user,db: Session=Depends(get_db)):
    # user_create=User(**request.dict())# for dynamic value insert


    # hashed_pswd=psw_cxt.hash(request.password) # for this we have created another class 
    hashed_pswd_class=Hash.dcrypt(request.password)
    user_data=request.dict()
    # user_data["password"]=hashed_pswd # for manually insert value for password dict

    user_data["password"]=hashed_pswd_class
    user_create=User(**user_data)
    db.add(user_create)
    db.commit()
    db.refresh(user_create)
    return user_create


def get_user_id(id:int,db:Session=Depends(get_db)):
    get_user=db.query(User).filter(User.id==id).first()
    if not get_user:
        raise HTTPException(status_code=404,detail=f"user not found with {id} id")
    return get_user


def delete_user(id:int,db:Session=Depends(get_db)):
    delete_us=db.query(User).filter(User.id==id).first()
    db.delete(delete_us)
    db.commit()
    return "delete susccess"