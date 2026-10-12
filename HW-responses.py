from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

class Product(BaseModel):
    name: str = Field(min_length=2)
    price: float = Field(gt=0)
    quantity: int = Field(gt=0)
    category: str

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category: str
    message: str

products = [
    {
        "id": 1,
        "name": "Keyboard",
        "price": 1200,
        "quantity": 10,
        "category": "Computer"
    },
    {
        "id": 2,
        "name": "Mouse",
        "price": 600,
        "quantity": 15,
        "category": "Computer"
    },
    {
        "id": 3,
        "name": "Monitor",
        "price": 8000,
        "quantity": 5,
        "category": "Electronics"
    },
    {
        "id": 4,
        "name": "Chair",
        "price": 3000,
        "quantity": 20,
        "category": "Furniture"
    }
]

@app.get("/products")
def get_products(category: str = None):
    if category:
        filtered = []
        for p in products:
            if p["category"].lower() == category.lower():
                filtered.append(p)
        return JSONResponse(
            status_code=200,
            content={
                "status": "success",
                "message": f"Products filtered by category '{category}'",
                "total_products": len(filtered),
                "data": filtered
            }
        )
    return {
        "status": "success",
        "message": "Products retrieved successfully",
        "total_products": len(products),
        "data": products
    }

@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {
                "status": "success",
                "message": "Product found successfully",
                "data": product
            }
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Product not found",
            "data": None
        }
    )

@app.post("/products", status_code=201)
def create_product(product: Product):
    new_id = len(products) + 1
    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
    products.append(new_product)
    return {
        "status": "success",
        "message": "Product created successfully",
        "data": new_product
    }

@app.post("/products/with-response-model", response_model=ProductResponse, status_code=201)
def create_product_with_response_model(product: Product):
    new_id = len(products) + 1
    new_product = {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category
    }
    products.append(new_product)
    return {
        "id": new_id,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity,
        "category": product.category,
        "message": "Product created successfully"
    }
