from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter, Form
from fastapi.security import OAuth2PasswordRequestForm
from uuid import uuid4
from auth.user import User, UserLogin, UserSignUp, UserInDB
from auth.token_model import Token
from auth.auth_handler import(
    authenticate_user,
    get_current_active_user ,
    create_access_token,
    get_hashed_password
)


router = APIRouter()

@router.post('/signup', summary="Create new user", response_model=User)
async def create_user(form_data: UserSignUp = Depends()):
    userdb = UserInDB(username=form_data.username, email= form_data.email, full_name=form_data.full_name, disabled= form_data.disabled, password=get_hashed_password(form_data.password))
    await userdb.create()
    return userdb

@router.post("/login/token", summary="User Login", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    # this function is going to authenticate the user and returns the user entity
    user = await authenticate_user(db = UserInDB, username=form_data.username, password=form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    # upon findng the user entity it will create an access token, that lasts about 30 minutes.
    access_token = create_access_token(subject=user.username)
    # then it will return the access token
    return Token(access_token=access_token, token_type="bearer")


@router.get("/me/", response_model=User)

async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

