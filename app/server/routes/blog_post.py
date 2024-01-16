from typing import List, Annotated
from urllib.parse import unquote
from fastapi import APIRouter, HTTPException, Depends, Form
from server.models.blog_post import Article, Comments
from auth.auth_user import User
from beanie import PydanticObjectId
from bson import ObjectId
from datetime import datetime
from auth.auth_handler import get_current_active_user 

router = APIRouter()

@router.post("/create", response_description="Blog added to the Database.")
async def add_blog_post(current_user: Annotated[User, Depends(get_current_active_user)], title=Form(...), content=Form(...)) -> dict:
    blog = Article(title=title, content=content, date=datetime.now(), author=current_user.username)
    post = await blog.create()
    return {"message": "Blog posted successfully!",
            "blog": post}

@router.get("/my_posts/all", response_description="Posts by me")
async def get_my_posts(current_user: Annotated[User, Depends(get_current_active_user)])-> List[Article]:
    posts = await Article.find({"author": current_user.username},sort=[("date", -1)]).to_list()
    if not posts:
        raise HTTPException(status_code=404, detail=f"You haven't posted anything yet")
    return posts

@router.post("/all/author={author}", response_description="Posts by an author")
async def get_blogs_by_author(author: str) -> List[Article]:
    posts = await Article.find({"author": unquote(author)},sort=[("date", -1)]).to_list()
    
    if not posts:
        raise HTTPException(status_code=404, detail=f"No posts found for the author {author}")
    
    return posts

@router.get("/read/id={id}")
async def read_a_blog(id: PydanticObjectId) -> Article:
    blog = await Article.get(id)
    return blog

@router.post("/comments/create/")
async def add_a_comment(comment: Comments) -> dict:
    post = await comment.create()
    return {"message": "Comment posted successfully!",
            "comment": post}
    
@router.get("/comments/read/article_id={article_id}")
async def read_all_comments(article_id: str) -> List[Comments]:
    comments = await Comments.find({"article_id": PydanticObjectId(article_id)},sort=[("date", -1)]).to_list()
    return comments
