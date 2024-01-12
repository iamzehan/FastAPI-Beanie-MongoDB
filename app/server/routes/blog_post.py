from typing import List
from urllib.parse import unquote
from fastapi import APIRouter, HTTPException
from server.models.blog_post import Article, Comments

router = APIRouter()

@router.post("/create", response_description="Blog added to the Database.")
async def add_blog_post(blog: Article) -> dict:
    post = await blog.create()
    return {"message": "Blog posted successfully!",
            "blog": post}

@router.post("/all/author={author}", response_description="Posts by an author")
async def get_blogs_by_author(author: str) -> List[Article]:
    posts = await Article.find({"author": unquote(author)},sort=[("date", -1)]).to_list()
    
    if not posts:
        raise HTTPException(status_code=404, detail=f"No posts found for the author {author}")
    
    return posts

@router.post("/comments/create/")
async def add_a_comment(comment: Comments) -> dict:
    comment = await comment.create()

    return {"message": "Comment posted successfully!",
            "comment": comment}
    
@router.get("/comments/read/article_id={article_id}")
async def read_all_comments(article_id: str) -> List[Comments]:
    comments = await Comments.find({"article_id": unquote(article_id)},sort=[("date", -1)]).to_list()
    return comments
