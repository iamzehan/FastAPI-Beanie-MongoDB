from typing import Optional
from beanie import Document
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

class User(Document):

    username: str

    email: Optional[EmailStr] = None

    full_name: Optional[str] = None
    
    disabled: Optional[bool] = None
    
    class Settings:
        name = "users_collection"
    
    model_config = {
        "json_schema_extra":{
            "examples":[
                {
                "username": "iamzehan",
                "email": "zehan@example.com",
                "full_name": "Md. Ziaul Karim",
                "password" : "12345",
                "diabled" : False
                }
            ]
        }
    }
class UserInDB(User):
    password : str
