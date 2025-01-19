from sqlalchemy.orm import Session
from schemas import ProductUpdate, ProductCreate
from models import ProductModel

def get_products(db: Session):
    """
    Retrieve all products from the database.

    Args:
        db (Session): SQLAlchemy database session.

    Returns:
        list: A list of all ProductModel instances in the database.
    """
    return db.query(ProductModel).all()

def get_product(db: Session, product_id: int):
    """
    Retrieve a specific product by its ID.

    Args:
        db (Session): SQLAlchemy database session.
        product_id (int): The ID of the product to retrieve.

    Returns:
        ProductModel or None: The product with the specified ID, or None if not found.
    """
    return db.query(ProductModel).filter(ProductModel.id == product_id).first()

def create_product(db: Session, product: ProductCreate):
    """
    Create a new product in the database.

    Args:
        db (Session): SQLAlchemy database session.
        product (ProductCreate): An instance of ProductCreate containing product details.

    Returns:
        ProductModel: The newly created product instance.
    """
    db_product = ProductModel(**product.model_dump())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product_id: int):
    """
    Delete a product from the database by its ID.

    Args:
        db (Session): SQLAlchemy database session.
        product_id (int): The ID of the product to delete.

    Returns:
        ProductModel or None: The deleted product instance, or None if not found.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    db.delete(db_product)
    db.commit()
    return db_product


def update_product(db: Session, product_id: int, product: ProductUpdate):
    """
    Update the details of an existing product.

    Args:
        db (Session): SQLAlchemy database session.
        product_id (int): The ID of the product to update.
        product (ProductUpdate): An instance of ProductUpdate containing updated product details.

    Returns:
        ProductModel or None: The updated product instance, or None if the product is not found.
    """
    db_product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if db_product is None:
        return None

    if product.name is not None:
        db_product.name = product.name
    if product.description is not None:
        db_product.description = product.description
    if product.price is not None:
        db_product.price = product.price
    if product.category is not None:
        db_product.category = product.category
    if product.supplier_email is not None:
        db_product.supplier_email = product.supplier_email

    db.commit()
    return db_product