from passlib.context import CryptContext

psw_cxt=CryptContext(schemes=["bcrypt"], deprecated="auto")
class Hash():
    def dcrypt(password:str):
        return psw_cxt.hash(password)
    
    def verify(hashed_password,plain_password):
        return psw_cxt.verify(plain_password,hashed_password)
