from fastapi import APIRouter, Depends, HTTPException
from shop_app.database.models import SubCategory
from shop_app.database.schema import SubCategoryInputSchema, SubCategoryOutSchema
from shop_app.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


subcategory_router = APIRouter(prefix='/subcategory', tags=['Subcategory'])


@subcategory_router.post("/", response_model=SubCategoryOutSchema)
async def create_subcategory(subcategory: SubCategoryInputSchema, db: Session = Depends(get_db)):
    subcategory_db = SubCategory(**subcategory.dict())
    db.add(subcategory_db)
    db.commit()
    db.refresh(subcategory_db)
    return subcategory_db


@subcategory_router.get("/", response_model=List[SubCategoryOutSchema])
async def list_subcategories(db: Session = Depends(get_db)):
    return db.query(SubCategory).all()


@subcategory_router.get('/{subcategory_id}', response_model=SubCategoryOutSchema)
async def detail_subcategory(subcategory_id: int, db: Session = Depends(get_db)):
    subcategory = db.query(SubCategory).filter(SubCategory.id == subcategory_id).first()
    if not subcategory:
        raise HTTPException(status_code=404, detail="мындай id субкатегория жок")
    return subcategory