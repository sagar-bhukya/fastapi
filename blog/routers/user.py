from fastapi import APIRouter,Depends,status,HTTPException
from typing import List
from schemas import response_Blog,BlogCreate,showUser,schema_user
from database import get_db
from models import Blog,User
from sqlalchemy.orm import Session
from hashing import Hash

from repository import user

router=APIRouter(
    prefix="/user",
    tags=["users"]
)


@router.post('/',response_model=showUser) # this will show only name and email.    tags=["users"]
def create_user(request:schema_user,db: Session=Depends(get_db)):
    # # user_create=User(**request.dict())# for dynamic value insert


    # # hashed_pswd=psw_cxt.hash(request.password) # for this we have created another class 
    # hashed_pswd_class=Hash.dcrypt(request.password)
    # user_data=request.dict()
    # # user_data["password"]=hashed_pswd # for manually insert value for password dict

    # user_data["password"]=hashed_pswd_class
    # user_create=User(**user_data)
    # db.add(user_create)
    # db.commit()
    # db.refresh(user_create)
    # return user_create
    return user.create_user(request,db)



#get id of user
@router.get('/{id}',response_model=showUser)#,tags=["users"]
def get_user_id(id:int,db:Session=Depends(get_db)):
    # get_user=db.query(User).filter(User.id==id).first()
    # if not get_user:
    #     raise HTTPException(status_code=404,detail=f"user not found with {id} id")
    # return get_user
    return user.get_user_id(id,db)



@router.delete('/{id}')#,tags=["users"]
def delete_user(id:int,db:Session=Depends(get_db)):
    # delete_us=db.query(User).filter(User.id==id).first()
    # db.delete(delete_us)
    # db.commit()
    # return "delete susccess"
    return user.delete_user(id,db)
