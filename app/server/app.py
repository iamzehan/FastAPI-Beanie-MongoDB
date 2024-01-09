from fastapi import FastAPI
from server.database import init_db
from server.routes.product_review import router as Router


app = FastAPI(docs_url="/")
app.include_router(Router, tags=["Product Reviews"], prefix="/reviews")


@app.on_event("startup")
async def start_db():
    await init_db()
    
@app.get("/root", tags=["Root"])
async def read_root() -> dict:
    return {"message": "This is Beanie Powered App!"}

