from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI()

# 1. REQUEST MODEL / Pydantic Schema
class Product(BaseModel):
    name: str = Field(min_length=2)       # Product name must be at least 2 characters
    price: float = Field(gt=0)            # Price must be greater than 0
    quantity: int = Field(gt=0)           # Quantity must be greater than 0
    category: str                         # Product category

# 2. RESPONSE MODEL
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    quantity: int
    category: str
    message: str                          # Extra message for clarity

# Fake database (matrix of products)
products = [
    {"id": 1, "name": "Keyboard", "price": 1200, "quantity": 10, "category": "Computer"},
    {"id": 2, "name": "Mouse", "price": 600, "quantity": 15, "category": "Computer"},
    {"id": 3, "name": "Monitor", "price": 8000, "quantity": 5, "category": "Electronics"}
]

# 3. RESPONSE FORMATTING - Get all products
@app.get("/products")
def get_products():
    return {
        "status": "success",
        "message": "Products retrieved successfully",
        "total_products": len(products),
        "data": products
    }

# 4. RESPONSE FORMATTING - Get single product by ID
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

# 5. STATUS CODE - Create product
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

# 6. RESPONSE MODEL - Create product with response model
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

# 7. JSONRESPONSE - Delete product
@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            products.remove(product)
            return JSONResponse(
                status_code=200,
                content={
                    "status": "success",
                    "message": "Product deleted successfully",
                    "deleted_product": product
                }
            )
    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Product not found"
        }
    )
