from typing import Optional
from beanie import Document
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import EmailStr, BaseModel


class User(Document):

    username: str

    email: Optional[EmailStr] = None

    full_name: Optional[str] = None
    
    disabled: Optional[bool] = False
    
    class Settings:
        name = "users_collection"
    
class UserInDB(User):
    password : str = "ExamplePassword"
    
    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                "username": "iamzehan",
                "email": "zehan@example.com",
                "full_name": "Md. Ziaul Karim",
                "diabled" : False,
                "password" : "12345"
                }
            ]
        }
    }
    
class UserSignUp(BaseModel):
    username: str

    email: Optional[EmailStr] = None

    full_name: Optional[str] = None
    
    disabled: Optional[bool] = False
    
    password : str
    
class UserLogin(OAuth2PasswordRequestForm):
    username: str
    password: str
