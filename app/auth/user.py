from typing import Optional
from beanie import Document
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
    
class UserLogin(BaseModel):
    username: str
    password: str
