from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
app = FastAPI()

# 3 sample datasets
data = [
    {
        "name": "Md. Jubayer Hasan",
        "age": 38,
        "gmail": "jubayerhasanshiplu@gmail.com",
        "password": "421292abc",
        "contact": 1734200012
    },
    {
        "name": "Shahnaz Sultana",
        "age": 35,
        "gmail": "shahnazsultana3212@outlook.com",
        "password": "8808884598",
        "contact": 1919421292
    },
    {
        "name": "Rayaan Tasnim",
        "age": 13,
        "gmail": "rayaantasnim@gmail.com",
        "password": "rayaan421292",
        "contact": 1919200012
    }
]

#Base Schema
class userCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=8, le=100)
    gmail: EmailStr
    password: str = Field(min_length=8)
    contact: int

#Post methode for the sign up
@app.post("/signup")
def signUp(user:userCreate):
    for i in data:
        if i["gmail"]==user.gmail:
            return{
                "Error": "User already exist ! Try log-in!"
            }

    data.append(user.model_dump())
    return{
        "message:" : "Sign Up successful!"
    }


@app.get("/all")
def show():
    return data