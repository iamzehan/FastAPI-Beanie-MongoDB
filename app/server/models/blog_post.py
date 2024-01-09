from beanie import Document
from datetime import datetime

class Article(Document):
    title: str
    content: str
    date: datetime = datetime.now()
    author: str
    
    class Settings:
        name = "articles_collection"
    
    class Config:
        schema_extra = {
            "example": {
                "title" : "Learn MongoDB and FastAPI",
                "content": "Today we are going to learn \
                            to use a Beanie Powered API with \
                            MongoDB and FastAPI",
                "date" : "1/9/2024 at 8:56 PM",
                "author" : "iamzehan"
            }
        } 
        
class Comments(Document):
    article_id: str
    content: str
    date: datetime = datetime.now()
    owner: str
    
    class Settings:
        collection_name = "comments_collection"
    
    class Config:
        example = {
            "example_article": {
                "article_id": "2034808asdkj3",
                "content": "Why do we use Beanie?",
                "date" : "1/9/2024 at 9:32 PM",
                "owner" : "ziaul"
            }
        } 
