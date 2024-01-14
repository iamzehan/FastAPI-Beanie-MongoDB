from typing import Annotated

from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordRequestForm

from auth.user import User, UserLogin
from auth.token_model import Token
from auth.auth_handler import(
    authenticate_user,
    get_current_active_user ,
    create_access_token
)


router = APIRouter()

@router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends(UserLogin)]
) -> Token:
    user = authenticate_user(User, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(subject=user.username)
    return Token(access_token=access_token, token_type="bearer")


@router.get("/users/me/", response_model=User)
async def read_users_me(
    current_user: Annotated[User, Depends(get_current_active_user)]
):
    return current_user

