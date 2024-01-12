from urllib.parse import unquote
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from server.models.blog_post import Article, Comments

router = APIRouter()

@router.post("/create", response_description="Blog added to the Database.")
async def add_blog_post(blog: Article) -> JSONResponse:
    """
    Endpoint to add a new blog post to the database.
    """
    post = await blog.create()
    return JSONResponse(
        content={"message": "Blog posted successfully!", "blog": post},
        status_code=201,
    )

@router.post("/all/author={author}", response_description="Posts by an author")
async def get_blogs_by_author(author: str) -> JSONResponse:
    """
    Endpoint to retrieve blog posts by a specific author.
    """
    posts = await Article.find({"author": unquote(author)}, sort=[("date", -1)]).to_list()
    
    if not posts:
        raise HTTPException(status_code=404, detail=f"No posts found for the author {author}")

    return JSONResponse(
        content={"message": f"Posts by author {author}", "posts": posts},
        status_code=200,
    )

@router.post("/comments/create/", response_description="Comment added successfully.")
async def add_a_comment(comment: Comments) -> JSONResponse:
    """
    Endpoint to add a comment to a blog post.
    """
    comment = await comment.create()
    return JSONResponse(
        content={"message": "Comment posted successfully!", "comment": comment},
        status_code=201,
    )
    
@router.get("/comments/read/article_id={article_id}", response_description="Retrieve comments for a blog post.")
async def read_all_comments(article_id: str) -> JSONResponse:
    """
    Endpoint to retrieve all comments for a specific blog post.
    """
    comments = await Comments.find({"article_id": unquote(article_id)}, sort=[("date", -1)]).to_list()
    return JSONResponse(
        content={"message": f"Comments for article {article_id}", "comments": comments},
        status_code=200,
    )
