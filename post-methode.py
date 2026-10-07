from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

data = [
    {"p_id": 1, 
     "p_name": "Book", 
     "p_price": 100, 
     "p_quantity": 24
     },

    {"p_id": 2, 
     "p_name": "Pen", 
     "p_price": 10, 
     "p_quantity": 200},

    {"p_id": 3, 
     "p_name": "Note Book", 
     "p_price": 100, 
     "p_quantity": 200},
]


@app.get("/")
def home():
    return {
        "Massage":"Welcome"
    }


#Schema Format
class productCreate(BaseModel):
    p_id:int
    p_name:str
    p_price:int
    p_quantity:int 


@app.post("/add/product")
def add_product(product:productCreate):
    data.append(product.model_dump())
    return{
        "Massage:":"Product Added"
    }


@app.get("/get/data")
def get_data():
    return data 

#Query parameter -> for quantity check ups 
@app.get("/get_products_by_quantity")
def get_products_by_price(quantity: int):
    products = []

    for i in data:
        if i["p_quantity"] == quantity:
            products.append(i)

    if len(products) == 0:
        return {
            "message": "Product not found!"
        }
    return products
