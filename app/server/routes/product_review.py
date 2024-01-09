from typing import List
from urllib.parse import unquote
from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from server.models.product_review import ProductReview, UpdateProductReview


router = APIRouter()

@router.post("/add", response_description="Review added to the database")
async def add_product_review(review: ProductReview) -> dict:
    # we use create() function from beanie Documents
    await review.create()
    return {"message": "Review added successfully"}

@router.get("/{id}", response_description="Review record retrieved")
async def get_review_record(id: PydanticObjectId) -> ProductReview:
    #We use get() function from beanie Documents
    review = await ProductReview.get(id)
    return review

@router.get("/all/rating={rated}", response_description="Reviews with the same rating", response_model=List[ProductReview])
async def get_reviews_by_rating(rated: float) -> List[ProductReview]:
    try:
        reviews = await ProductReview.find(ProductReview.rating == rated).to_list()
        if not reviews:
            raise HTTPException(status_code=404, detail=f"No reviews found for the rating {rated}.")
        return reviews
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")  

@router.get("/all/product='{product_name}'", response_description="Review records retrieved")
async def get_reviews(product_name: str) -> List[ProductReview]:
    decoded_product_name = unquote(product_name)
    print(f"Decoded Product Name: {decoded_product_name}")

    try:
        reviews = await ProductReview.find(ProductReview.product == decoded_product_name).to_list()
        if not reviews:
            raise HTTPException(status_code=404, detail=f"No reviews found for the product {decoded_product_name}.")
        return reviews
    except Exception as e:
        print(f"Exception during review retrieval: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")

@router.put("/update/{id}", response_description="Review record updated")
async def update_review_data(id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k: v for k, v in dict(req).items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await review.update(update_query)
    return review

@router.delete("/delete/{id}", response_description="Review record deleted from the database")
async def delete_review_data(id: PydanticObjectId) -> dict:
    record = await ProductReview.get(id)

    if not record:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await record.delete()
    return {
        "message": "Record deleted successfully"
    }