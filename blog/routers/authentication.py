
from sqlalchemy.orm import Session
from database import get_db
from fastapi import APIRouter,Depends,HTTPException
from schemas import Login
from models import User
from hashing import Hash
from my_token import create_access_token
from fastapi.security import OAuth2PasswordRequestForm
router=APIRouter(
    tags=["authentication"]
)

@router.post('/login')
def login(request: OAuth2PasswordRequestForm =Depends(),db:Session=Depends(get_db)):
    user=db.query(User).filter(User.email==request.username).first()
    if not user:
        raise HTTPException(status_code=404,detail="invalid credentials")
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=404,detail="incorrect password")
    
    access_token=create_access_token(data={"sub":user.email})
    return {"access_token":access_token,"token_type":"bearer"}

