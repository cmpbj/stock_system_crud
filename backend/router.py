from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, get_db
from schemas import ProductResponse, ProductUpdate, ProductCreate
from typing import List
from crud import (
    create_product,
    get_products,
    get_product,
    delete_product,
    update_product,
)

router = APIRouter()

@router.get("/")
def read_root():
    """
    Root endpoint of the API.

    """
    return {"message": "Stock Menagement API"}

@router.get("/products/", response_model=List[ProductResponse])
def read_all_products_route(db: Session = Depends(get_db)):
    """
    Retrieve all products from the database.

    """
    products = get_products(db)
    return products

@router.get("/products/{product_id}", response_model=ProductResponse)
def read_one_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Retrieve a specific product by its ID.

    """
    product = get_product(db=db, product_id=product_id)
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ProductResponse)
def create_product_route(product: ProductCreate, db: Session = Depends(get_db)):
    """
    Create a new product in the database.

    """
    return create_product(db=db, product=product)

@router.delete("/products/{product_id}", response_model=ProductResponse)
def delete_product_route(product_id: int, db: Session = Depends(get_db)):
    """
    Delete a product from the database by its ID.

    """
    product_db = delete_product(db=db, product_id=product_id)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_db

@router.put("/products/{product_id}", response_model=ProductResponse)
def update_product_route(product_id: int, product: ProductUpdate, db: Session = Depends(get_db)):
    """
    Update an existing product in the database.

    """
    product_db = update_product(db=db, product_id=product_id, product=product)
    if product_db is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product_db
