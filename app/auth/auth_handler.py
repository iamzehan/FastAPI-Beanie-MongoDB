import os

from dotenv import load_dotenv
from jose import jwt, JWTError

from typing import Union, Any, Annotated
from datetime import datetime, timedelta

from app.auth.auth_user import User, UserInDB
from app.auth.auth_token import TokenData

from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# load the .env file
load_dotenv()

# let's determine the defaults
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30 minutes
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # 7 days

# following are the secrets
ALGORITHM = os.environ['ALGORITHM']
JWT_SECRET_KEY = os.environ['SECRET_KEY']
JWT_REFRESH_SECRET_KEY = os.environ['REFRESH_SECRET_KEY'] 

# this is an instance to your password_context, that can encrypt and decrypt your password, verify them etc.
password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/user/login/token")

# ---- HASHING PASSWORDS ---- 
def get_hashed_password(password: str) -> str:
    # this function hashes your password and returns it
    return password_context.hash(password)

# ---- VERIFY HASHED PASSWORD
def verify_password(password: str, hashed_pass: str) -> bool:
    # this function varifies your password
    return password_context.verify(password, hashed_pass)

# ---- GET USER FROM DATABASE ----
async def get_user(db: User, username: str):
    user = await db.find_one(db.username==username)
    return user

# ---- AUTHENTICATION w/ USERNAME, PASSWORD ----
async def authenticate_user(db: UserInDB, username: str, password: str):
    # we find the username in the database
    user = await db.find_one(db.username ==  username)
    if not user:
        return False
    # if the user is found, we then verify the password, with the stored hashed password
    if not verify_password(password, user.password):
        return False
    # after verification we return the user entity
    return user

# ---- GET CURRENT USER ----
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # this right here decodes the jwt token 
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        # then stores the subject from payload as username
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        # then it sets the token data according to the username
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    # then it gets the user from the database by separating username from the token data
    user = await get_user(db=User, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

# this function gets the current active user
async def get_current_active_user(current_user: User = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user

# this function creates an access token, it also determines when your token expires
def create_access_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        # if there is an expiration time given, then it sets it accordingly
        expires_delta = datetime.utcnow() + expires_delta
    else:
        # otherwise it sets the expiration time to default
        expires_delta = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        
    # now we determine how to encode our jwt token, with time delta and subject
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    # now we encode our jwt, with the secret and the algorithm
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

# this function is responsible for refreshing your token every seven days
def create_refresh_token(subject: Union[str, Any], expires_delta: int = None) -> str:
    if expires_delta is not None:
        # if there is an expiration time given, then it sets it accordingly
        expires_delta = datetime.utcnow() + expires_delta
    else:
        # otherwise it sets the expiration time to default
        expires_delta = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    # now we determine how to encode our jwt token, with time delta and subject
    to_encode = {"exp": expires_delta, "sub": str(subject)}
    # now we encode our jwt, with the secret and the algorithm
    encoded_jwt = jwt.encode(to_encode, JWT_REFRESH_SECRET_KEY, ALGORITHM)
    return encoded_jwt