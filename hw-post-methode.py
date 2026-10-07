from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

data = [
    {
        "title": "Nondito Noroke",
        "author": "Humayun Ahmed",
        "year": 1972,
        "price": 2.50,
    },
    {
        "title": "Hajar Bochor Dhore",
        "author": "Zahir Raihan",
        "year": 1964,
        "price": 3.20,
    },
    {
        "title": "A Golden Age",
        "author": "Tahmima Anam",
        "year": 2007,
        "price": 14.95,
    },
    {
        "title": "Chilerkothar Sepai",
        "author": "Akhteruzzaman Elias",
        "year": 1986,
        "price": 6.50,
    },
    {
        "title": "Lalsalu",
        "author": "Syed Waliullah",
        "year": 1948,
        "price": 4.00,
    },
    {
        "title": "Jochna O Jononir Golpo",
        "author": "Humayun Ahmed",
        "year": 2004,
        "price": 8.50,
    },
    {
        "title": "In the Light of What We Know",
        "author": "Zia Haider Rahman",
        "year": 2014,
        "price": 16.99,
    },
    {
        "title": "Amar Bondhu Rashed",
        "author": "Muhammad Zafar Iqbal",
        "year": 1996,
        "price": 3.50,
    },
    {
        "title": "Sultana's Dream",
        "author": "Begum Rokeya Sakhawat Hossain",
        "year": 1905,
        "price": 1.99,
    },
]



@app.get("/")
def home():
    return {"Message": "Welcome to Book Collection API"}


# Schema Format
class BookCreate(BaseModel):
    title: str
    author: str
    year: int
    price: float


@app.post("/books")
def add_book(book: BookCreate):
    data.append(book.model_dump())
    return {"Message": "Book successfully added to the collection!"}


@app.get("/get/data")
def get_data():
    return data


# Query parameter -> for year check ups
@app.get("/get_books_by_year")
def get_books_by_year(year: int):
    books = []

    for i in data:
        if i["year"] == year:
            books.append(i)

    if len(books) == 0:
        return {"Message": "Book not found!"}
    return books
