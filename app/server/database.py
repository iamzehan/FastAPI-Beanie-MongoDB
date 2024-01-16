from beanie import init_beanie
import motor.motor_asyncio
from auth.auth_user import User
from server.models.blog_post import Article, Comments
from server.models.product_review import ProductReview

async def init_db():
    client = motor.motor_asyncio.AsyncIOMotorClient(
        "mongodb://localhost:27017/"
    )

    await init_beanie(database=client.blog_review, document_models=[ProductReview, Article, Comments, User])
    
    