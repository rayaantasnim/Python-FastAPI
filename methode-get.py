from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome!"}

@app.get("/websites")
def show_products():
    return {
        "Name": "Rayaan Tasnim",
        "GitHub Repo": "74",
        "CodeForces Rating": "519",
    }

@app.get("/websites/prime-factors")
def prime_factor():
    return {
        "Topic": "Rayaan Tasnim's websites based on prime factorization",
        "Number of Projects": "3",
        "Sandbox capability": "10 to the power 40",
    }

@app.get("/product")
def show():
    return "Product"

@app.get("/product/{id}")
def get_product(id:int):
    return{
        "massage":id+10
    }