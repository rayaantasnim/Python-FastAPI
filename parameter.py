from fastapi import FastAPI
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

    {"p_id": 4, 
     "p_name": "Pencil", 
     "p_price": 5, 
     "p_quantity": 150},
    
    {"p_id": 5, 
     "p_name": "Eraser", 
     "p_price": 3, 
     "p_quantity": 80},
    
    {"p_id": 6, 
     "p_name": 
     "Ruler", 
     "p_price": 15, 
     "p_quantity": 50
     },
    
    {"p_id": 7, 
     "p_name": "Marker", 
     "p_price": 20, 
     "p_quantity": 120
     }
]

@app.get("/")
def home():
    return {
        "message": "Welcome !"
    }

@app.get("/products")
def show_products():
    return data

@app.get("/get_product/{id}")
def get_product(id: int):
    for i in data:
        if i["p_id"] == id:
            return i
    return {
        "message": "Product not found"
    }


@app.get("/get_products_by_price")
def get_products_by_price(price: int):
    products = []
    for i in data:
        if i["p_price"] == price:
            products.append(i)
    if len(products) == 0:
        return {
            "message": "Product not found"
        }
    return products
