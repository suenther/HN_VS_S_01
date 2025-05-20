from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import SessionLocal, engine
import models

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/products", response_model=models.ProductRead)
def create_product(product: models.ProductCreate, db: Session = Depends(get_db)):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

@app.get("/products", response_model=list[models.ProductRead])
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/products/search/{name}", response_model=list[models.ProductRead])
def search_products(name: str, db: Session = Depends(get_db)):
    return db.query(models.Product).filter(models.Product.name.contains(name)).all()


@app.get("/products", response_model=list[models.ProductRead])
def read_products(db: Session = Depends(get_db)):
    return db.query(models.Product).all()

@app.get("/products-raw")
def raw_query(db: Session = Depends(get_db)):
    result = db.execute(text("SELECT * FROM products"))
    rows = result.fetchall()
    return [row._mapping for row in rows]