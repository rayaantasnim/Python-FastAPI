from fastapi import FastAPI
from fastapi.responses import JSONResponse

# Create FastAPI application instance
app = FastAPI()

# Fake database (matrix of users)
users_db = [
    {"id": 1, "name": "Rahim", "age": 25, "email": "rahim@example.com"},
    {"id": 2, "name": "Karim", "age": 30, "email": "karim@example.com"},
    {"id": 3, "name": "Selim", "age": 28, "email": "selim@example.com"},
    {"id": 4, "name": "Anika", "age": 22, "email": "anika@example.com"},
    {"id": 5, "name": "Rafiq", "age": 35, "email": "rafiq@example.com"}
]

# Endpoint to get all users
@app.get("/users")
def get_all_users():
    # Return the entire database
    return JSONResponse(
        status_code=200,
        content={"users": users_db}
    )

# Endpoint to get a single user by ID
@app.get("/user/{user_id}")
def get_user(user_id: int):
    # Search for user in the database
    for user in users_db:
        if user["id"] == user_id:
            return JSONResponse(
                status_code=200,
                content={"user": user}  # Return user details
            )

    # If user not found
    return JSONResponse(
        status_code=404,
        content={"error": "User not found"}
    )
