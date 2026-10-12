from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
app = FastAPI()

# 4 sample datasets
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
        "name": "Rifah Tasnia",
        "age": 35,
        "gmail": "rifahtasnia@gmail.com",
        "password": "9889776878",
        "contact": 1919421290
    },

    {
        "name": "Rayaan Tasnim",
        "age": 13,
        "gmail": "rayaantasnim@gmail.com",
        "password": "rayaan421292",
        "contact": 1919200012
    }
]

#Base Schema - for Sign in
class userCreate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=8, le=100)
    gmail: EmailStr
    password: str = Field(min_length=8)
    contact: int

#Log in - schema 
class userLogin(BaseModel):
    email:EmailStr
    password:str = Field(min_length=8)

#Post methode for the sign up
@app.post("/signup")
def signUp(user: userCreate):
    for i in data:
        if i["gmail"]==user.gmail:
            return{
                "Error": "User already exist ! Try log-in!"
            }

    data.append(user.model_dump())
    return{
        "message:" : "Sign Up successful!"
    }


#Just deta showcase
@app.get("/all")
def show():
    return data


#Core Log in system

@app.post("/login")
def login(user: userLogin):
    for i in data:
        
        if i["gmail"] == user.email and i["password"] == user.password:
            return {
                "message": "Log in successful",
                "user_name": i["name"] 
            }
    return {
        "error": "Invalid email or password"
    }


#Query parameter for age based task
@app.get("/search_by_age")
def search_by_age(age: int):
    users = []
    for i in data:
        if i["age"] == age:

            user_info = {
                "name": i["name"],
                "contact": i["contact"],  
                "gmail": i["gmail"]
            }
            users.append(user_info)
            
    if len(users) == 0:
        return {
            "message": "User not found"
        }
    return users