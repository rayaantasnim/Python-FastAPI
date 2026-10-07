from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()
data = [
    {
        "p_id": 1, 
        "p_name": "Book", 
        "p_price": 150, 
        "p_quantity": 24
    },
    {
        "p_id": 2, 
        "p_name": "Pen Set", 
        "p_price": 120, 
        "p_quantity": 200
    },
    {
        "p_id": 3, 
        "p_name": "Note Book", 
        "p_price": 100, 
        "p_quantity": 200
    },
]

# Schema Format
class ProductCreate(BaseModel):
    p_id: int = Field(gt=0, lt=1000)
    p_name: str = Field(min_length=3, max_length=50)
    p_price: int = Field(ge=100, le=2000) 
    p_quantity: int = Field(ge=1)


@app.get("/")
def home():
    return {"message": "Welcome"}


@app.post("/add/product")
def add_product(product: ProductCreate):
    data.append(product.model_dump())
    return {"message": "Product Added"}


@app.get("/get/data")
def get_data():
    return data


# Query parameter -> for quantity check ups
@app.get("/get_products_by_quantity")
def get_products_by_quantity(quantity: int):
    products = []
    for i in data:
        if i["p_quantity"] == quantity:
            products.append(i)
            
    if len(products) == 0:
        return {"message": "Product not found!"}
        
    return products
