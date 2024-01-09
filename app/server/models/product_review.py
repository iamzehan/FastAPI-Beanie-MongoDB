from beanie import Document
from datetime import datetime
from pydantic import BaseModel
from typing import Optional



class ProductReview(Document):
    fullname: str 
    username: str
    product: str 
    rating: float 
    review: str
    date: datetime = datetime.now()
    
    class Settings:
        name = "product_review_collection"
    

    model_config = {
    "json_schema_extra":{
        "examples":[ {
            "fullname": "Md. Ziaul Karim",
            "username": "ziaul",
            "product": "FastAPI Tutorial w/ Tiangolo",
            "rating": 4.5,
            "review": "Great Course!",
            "date": datetime.now()
        }
        ]
        }
    }
    
class UpdateProductReview(BaseModel):
    fullname: Optional[str]
    username: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    model_config = {
        "json_schema_extra": {
            "examples":[ {
                "fullname": "Md. Ziaul Karim",
                "username": "ziaul",
                "product": "FastAPI Tutorial w/ Tiangolo",
                "rating": 5.5,
                "review": "Great Course!",
                "date": datetime.now()
            }
            ]
        }
    }