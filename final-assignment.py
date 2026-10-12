from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
app = FastAPI()

users_db = [
    {
        "name": "Md. Jubayer Hasan",
        "email": "jubayerhasanshiplu@gmail.com",
        "age": 38,
        "password": "421292abc"
    }
]

books_db = [
    {
        "id": 1, 
        "title": "Nondito Noroke", 
        "author": "Humayun Ahmed", 
        "category": "Drama", 
        "price": 150.0
    },
    {
        "id": 2, 
        "title": "Hajar Bochor Dhore", 
        "author": "Zahir Raihan", 
        "category": "Classic", 
        "price": 120.0
    },
    {
        "id": 3, 
        "title": "A Golden Age", 
        "author": "Tahmima Anam", 
        "category": "History", 
        "price": 350.0
    },
    {
        "id": 4, 
        "title": "Chilerkothar Sepai", 
        "author": "Akhteruzzaman Elias", 
        "category": "Drama", 
        "price": 280.0
    },
    {
        "id": 5, 
        "title": "Harry Potter", 
        "author": "J.K. Rowling", 
        "category": "Fantasy", 
        "price": 450.0
    }
]

class BookCreate(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(gt=0.0)

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    email: EmailStr
    age: int = Field(gt=0)
    password: str = Field(min_length=8)

class UserLogin(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8)

@app.post("/books")
def add_book(book: BookCreate):
    books_db.append(book.model_dump())
    return {"message": "Book successfully added to the collection!"}

@app.post("/signup")
def sign_up(user: UserCreate):
    for u in users_db:
        if u["email"] == user.email:
            return {"error": "User already exists! Try logging in."}
    users_db.append(user.model_dump())
    return {"message": "Sign Up successful!"}

@app.post("/login")
def login(user: UserLogin):
    for u in users_db:
        if u["email"] == user.email and u["password"] == user.password:
            return {"message": "Log in successful", "user_name": u["name"]}
    return {"error": "Invalid email or password"}

@app.get("/get/all/books")
def get_all_books():
    return books_db

@app.get("/get/book/{book_id}")
def get_book(book_id: int):
    for book in books_db:
        if book["id"] == book_id:
            return book
    return {"message": "Book not found"}

@app.get("/find/books")
def find_books_by_category(category: str):
    filtered = []
    for book in books_db:
        if book["category"] == category:
            filtered.append(book)
    if len(filtered) == 0:
        return {"message": "Book not found!"}
    return filtered

@app.get("/filter/books")
def filter_books_by_author(author: str):
    filtered = []
    for book in books_db:
        if book["author"] == author:
            filtered.append(book)
    if len(filtered) == 0:
        return {"message": "Book not found!"}
    return filtered
