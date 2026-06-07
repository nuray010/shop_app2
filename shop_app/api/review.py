from fastapi import APIRouter, Depends, HTTPException
from shop_app.database.models import Review
from shop_app.database.schema import ReviewInputSchema, ReviewOutSchema
from shop_app.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


review_router = APIRouter(prefix='/review', tags=['Review'])


@review_router.post("/", response_model=ReviewOutSchema)
async def create_review(review: ReviewInputSchema, db: Session = Depends(get_db)):
    review_db = Review(**review.dict())
    db.add(review_db)
    db.commit()
    db.refresh(review_db)
    return review_db


@review_router.get("/", response_model=List[ReviewOutSchema])
async def list_reviews(db: Session = Depends(get_db)):
    return db.query(Review).all()


@review_router.get('/{review_id}', response_model=ReviewOutSchema)
async def detail_review(review_id: int, db: Session = Depends(get_db)):
    review = db.query(Review).filter(Review.id == review_id).first()
    if not review:
        raise HTTPException(status_code=404, detail="мындай id пикир жок")
    return review