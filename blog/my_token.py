import secrets
# import logger
# import logging
# Generate a 32-byte (256-bit) random key
secret_key = secrets.token_hex(32)
print(secret_key)


from datetime import datetime, timedelta, timezone
from typing import Union
from jose import JWSError,jwt
from schemas import TokenData


SECRET_KEY="83c9ccf57bd63595a36357efb6776af5b3e046faf017e7f7871505c118ccb121"
ALGORITHM ="HS256"
ACCESS_TOKEN_EXPIRE_MINUTES=30



def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token:str,credentials_exception):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        email:str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email=email)
    except JWSError:
        raise credentials_exception