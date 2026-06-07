from fastapi import APIRouter, Depends, HTTPException
from shop_app.database.models import ProductImage
from shop_app.database.schema import ProductImageInputSchema, ProductImageOutSchema
from shop_app.database.db import SessionLocal
from sqlalchemy.orm import Session
from typing import List


async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


product_image_router = APIRouter(prefix='/product-image', tags=['Product_Image'])


@product_image_router.post("/", response_model=ProductImageOutSchema)
async def create_product_image(product_image: ProductImageInputSchema, db: Session = Depends(get_db)):
    product_image_db = ProductImage(**product_image.dict())
    db.add(product_image_db)
    db.commit()
    db.refresh(product_image_db)
    return product_image_db


@product_image_router.get("/", response_model=List[ProductImageOutSchema])
async def list_product_images(db: Session = Depends(get_db)):
    return db.query(ProductImage).all()


@product_image_router.get('/{product_image_id}', response_model=ProductImageOutSchema)
async def detail_product_image(product_image_id: int, db: Session = Depends(get_db)):
    product_image = db.query(ProductImage).filter(ProductImage.id == product_image_id).first()
    if not product_image:
        raise HTTPException(status_code=404, detail="мындай id сурот жок")
    return product_image