from fastapi import FastAPI
from server.database import init_db
from server.routes.product_review import router as ReviewRouter
from server.routes.blog_post import router as BlogRouter
from server.routes.user import router as UserRouter


app = FastAPI(docs_url="/")
app.include_router(UserRouter, tags=["Authentication"], prefix="/user")
app.include_router(ReviewRouter, tags=["Product Reviews"], prefix="/reviews")
app.include_router(BlogRouter, tags=["Blog Posts"], prefix="/blogs")

@app.on_event("startup")
async def start_db():
    await init_db()
    

