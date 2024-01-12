from beanie import Document
from datetime import datetime
from typing import Optional
from bson import ObjectId
class Article(Document):
    title: str
    content: str
    date: Optional[datetime] = datetime.now()
    author: str
    
    class Settings:
        name = "articles_collection"
    
    model_config= {
        "json_schema_extra":{
            "examples": [{
                "title" : "Learn MongoDB and FastAPI",
                "content": "Today we are going to learn to use a Beanie Powered API with MongoDB and FastAPI",
                "author" : "iamzehan"
            }
            ]
        } 
    }
        
class Comments(Document):
    article_id: str
    content: str
    date: Optional[datetime] = datetime.now()
    owner: str
    
    class Settings:
        name = "comments_collection"
    
    model_config = {
        "json_schema_extra":{
            "examples": [{
                "article_id" : "65a15a201b77ea7ebddb90c3",
                "content": "Why do we use Beanie?",
                "owner" : "ziaul"
            }]
        } 
    }
