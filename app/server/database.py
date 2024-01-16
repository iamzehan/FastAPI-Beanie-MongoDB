from beanie import init_beanie
import motor.motor_asyncio
from auth.auth_user import User
from server.models.blog_post import Article, Comments
from server.models.product_review import ProductReview

import os

from dotenv import load_dotenv

load_dotenv()

async def init_db():
    # we are accessing our connection string via environment variables
    # because it's not very wise to just keep it out in the open
    client = motor.motor_asyncio.AsyncIOMotorClient(os.environ['MONGODB_CONNECTION_STRING'])

    await init_beanie(database=client.blog_review, document_models=[ProductReview, Article, Comments, User])
    
    