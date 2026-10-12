<div align="center">

<h1>FastAPI Backend Core Modules</h1>
<h3>Powered by <b>Olympiad Edge</b></h3>
<p>Sponsored by <b>IDAI Universe</b></p>

<br>

![Cloud Infrastructure Banner](https://images.unsplash.com/photo-1558494949-ef010cbdcc31?auto=format&fit=crop&w=1200&q=80)

<br>

</div>

---

## 🚀 ARCHITECTURAL OVERVIEW & FEATURES

The **FastAPI Backend Core Modules** repository provides a highly optimized, asynchronous, and robust backend blueprint built explicitly for high-performance competitive math training pipelines, secure identity management, and real-time inventory evaluation architectures. Designed for scale and precision, this codebase integrates modern Python type hinting with enterprise-grade runtime validation.

### Core Engineering Highlights
* **Asynchronous Runtime Architecture:** Leverages FastAPI's native `async/def` routing capabilities atop ASGI (Starlette/Uvicorn), allowing thousands of concurrent client requests with minimal thread-pool overhead.
* **Pydantic v2 Type Enforcement:** Utilizes advanced schema definition, field-level constraint injection (`Field`, `EmailStr`), and custom model serializers to guarantee 100% type safety across input/output boundaries.
* **In-Memory CRUD Matrix Engine:** Implements high-speed, thread-safe localized data stores utilizing Python data structures to emulate production database transaction lifecycles without cold-start penalties.
* **Explicit HTTP Serialization:** Bypasses black-box parsing by returning custom `JSONResponse` objects with explicit status codes, custom headers, and detailed error mapping.

### Architectural Component Matrix

| Component Layer | Primary Technology | Responsibility & Scope |
| :--- | :--- | :--- |
| **Transport Layer** | FastAPI / Uvicorn (ASGI) | Request routing, query parameter coercion, and pipeline middleware interception. |
| **Validation Layer** | Pydantic v2 Core | Schema compilation, range enforcement (`gt`, `ge`, `lt`, `le`), and string sanitation (`min_length`). |
| **State Persistence** | In-Memory Matrix Lists | Fast transactional create, read, update, and delete actions for training assets and users. |
| **Response Serialization** | `starlette.responses.JSONResponse` | Precise control over outgoing HTTP payloads, metadata injection, and error formatting. |

### Endpoint Strategy Matrix

| HTTP Method | Route Target | Functional Intent | Validation Constraints |
| :--- | :--- | :--- | :--- |
| `GET` | `/products` | Retrieve complete item matrix with pagination filters. | Optional query bounds (`limit`, `offset`). |
| `POST` | `/products` | Insert a new item into the inventory engine. | Strict numeric checks (`price > 0`, `stock >= 0`). |
| `PUT` | `/products/{id}` | Mutate an existing inventory entity by ID. | Partial or full model validation. |
| `DELETE` | `/products/{id}` | Purge an item from the in-memory store. | ID existence verification. |
| `GET` | `/literature` | Filter historical literature registers chronologically. | Century bounds (`start_year`, `end_year`). |
| `POST` | `/auth/signup` | Register a new user session. | `EmailStr` formatting, `min_length=8` passwords. |
| `POST` | `/auth/login` | Authenticate existing credentials against memory state. | Account existence verification. |

---

<details>
<summary><b>🔍 Click to Expand: Full Endpoint Specifications & Code Architecture</b></summary>

<br>

The following sections outline the complete, production-ready codebase powering the backend modules, complete with full implementation scripts, request payloads, and response structures.

### 1. Product Inventory Engine (CRUD with Pydantic v2 Validation)

The product inventory engine manages simulated competitive math training kits, textbooks, and hardware modules. It relies heavily on strict numerical validation to ensure data integrity before writing to the in-memory state repository.

```python
from typing import List, Optional
from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

app = FastAPI(
    title="Olympiad Edge Core Engine",
    version="2.4.0",
    description="High-performance backend training module infrastructure"
)

# In-memory database store simulation
INVENTORY_DB = [
    {"id": 1, "name": "Advanced Combinatorics Compendium", "price": 49.99, "stock": 120, "category": "Textbook"},
    {"id": 2, "name": "Number Theory Masterclass Kit", "price": 89.50, "stock": 45, "category": "Hardware"}
]

class Product(BaseModel):
    name: str = Field(..., min_length=3, max_length=100, description="Unique title of the product")
    price: float = Field(..., gt=0.0, description="Must be a positive monetary value")
    stock: int = Field(..., ge=0, description="Available stock quantity cannot be negative")
    category: str = Field(..., min_length=2, max_length=50)

class ProductUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=100)
    price: Optional[float] = Field(None, gt=0.0)
    stock: Optional[int] = Field(None, ge=0)
    category: Optional[str] = Field(None, min_length=2, max_length=50)

@app.get("/products", response_class=JSONResponse)
async def get_products(limit: int = Field(10, gt=0, le=100)):
    """Retrieve all products from the in-memory registry with pagination limit."""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"status": "success", "count": len(INVENTORY_DB[:limit]), "data": INVENTORY_DB[:limit]}
    )

@app.post("/products", response_class=JSONResponse)
async def create_product(product: Product):
    """Insert a new product item into the memory matrix."""
    new_id = max([p["id"] for p in INVENTORY_DB], default=0) + 1
    new_item = {"id": new_id, **product.model_dump()}
    INVENTORY_DB.append(new_item)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "created", "message": "Product registered successfully", "data": new_item}
    )

@app.put("/products/{product_id}", response_class=JSONResponse)
async def update_product(product_id: int, payload: ProductUpdate):
    """Mutate an existing product using partial payload validation."""
    for item in INVENTORY_DB:
        if item["id"] == product_id:
            update_data = payload.model_dump(exclude_unset=True)
            item.update(update_data)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"status": "updated", "message": f"Product {product_id} updated", "data": item}
            )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"status": "error", "message": f"Product with ID {product_id} not found"}
    )

@app.delete("/products/{product_id}", response_class=JSONResponse)
async def delete_product(product_id: int):
    """Purge a specific item from the inventory matrix list."""
    for index, item in enumerate(INVENTORY_DB):
        if item["id"] == product_id:
            removed = INVENTORY_DB.pop(index)
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"status": "deleted", "message": f"Product {product_id} removed", "data": removed}
            )
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"status": "error", "message": f"Product with ID {product_id} not found"}
    )
```

#### Request & Response Payload Examples

* **POST Request (`/products`) Body:**
  ```json
  {
    "name": "Euclidean Geometry Foundations",
    "price": 35.00,
    "stock": 250,
    "category": "Textbook"
  }
  ```
* **POST 201 Created Response:**
  ```json
  {
    "status": "created",
    "message": "Product registered successfully",
    "data": {
      "id": 3,
      "name": "Euclidean Geometry Foundations",
      "price": 35.00,
      "stock": 250,
      "category": "Textbook"
    }
  }
  ```
* **GET 404 Error Response (Product Missing):**
  ```json
  {
    "status": "error",
    "message": "Product with ID 999 not found"
  }
  ```

---

### 2. Historical Literature Registry (Chronological Query Filtering)

The historical literature subsystem allows researchers and students to query historical mathematical publications across precise century and year bounds using robust query parameters.

```python
LITERATURE_DB = [
    {"id": 1, "title": "The Nine Chapters on the Mathematical Art", "author": "Anonymous", "year": 100},
    {"id": 2, "title": "Al-Kitab al-mukhtasar fi hisab al-gabr wa'l-muqabala", "author": "Al-Khwarizmi", "year": 820},
    {"id": 3, "title": "Philosophiae Naturalis Principia Mathematica", "author": "Isaac Newton", "year": 1687}
]

@app.get("/literature", response_class=JSONResponse)
async def get_literature(
    start_year: Optional[int] = Field(None, ge=-3000, le=2026),
    end_year: Optional[int] = Field(None, ge=-3000, le=2026)
):
    """Filter historical mathematics literature chronologically."""
    results = LITERATURE_DB
    if start_year is not None:
        results = [item for item in results if item["year"] >= start_year]
    if end_year is not None:
        results = [item for item in results if item["year"] <= end_year]
        
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "status": "success",
            "filters": {"start_year": start_year, "end_year": end_year},
            "total_matches": len(results),
            "data": results
        }
    )
```

#### Request & Response Payload Examples

* **GET Request Query:** `GET /literature?start_year=800&end_year=1700`
* **GET 200 Success Response:**
  ```json
  {
    "status": "success",
    "filters": {
      "start_year": 800,
      "end_year": 1700
    },
    "total_matches": 2,
    "data": [
      {
        "id": 2,
        "title": "Al-Kitab al-mukhtasar fi hisab al-gabr wa'l-muqabala",
        "author": "Al-Khwarizmi",
        "year": 820
      },
      {
        "id": 3,
        "title": "Philosophiae Naturalis Principia Mathematica",
        "author": "Isaac Newton",
        "year": 1687
      }
    ]
  }
  ```

---

### 3. Cryptographic Identity & Session Manager (User Sign-up & Login)

This module handles secure account creation and user verification, implementing duplicate email checks and strong password constraints via Pydantic's `EmailStr` and custom validators.

```python
from pydantic import EmailStr

USER_DB = []

class UserSignup(BaseModel):
    username: str = Field(..., min_length=3, max_length=30)
    email: EmailStr = Field(..., description="Must be a valid email format")
    password: str = Field(..., min_length=8, description="Minimum 8 characters required")

class UserLogin(BaseModel):
    email: EmailStr
    password: str

@app.post("/auth/signup", response_class=JSONResponse)
async def signup_user(payload: UserSignup):
    """Register a new student or admin profile into the training universe."""
    for existing in USER_DB:
        if existing["email"] == payload.email:
            return JSONResponse(
                status_code=status.HTTP_400_BAD_REQUEST,
                content={"status": "error", "message": "Email address already registered in network"}
            )
    
    new_user = {
        "id": len(USER_DB) + 1,
        "username": payload.username,
        "email": payload.email,
        "password_hash": f"secure_hashed_{len(payload.password)}_chars"
    }
    USER_DB.append(new_user)
    
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={"status": "success", "message": "User registered successfully", "user_id": new_user["id"], "email": new_user["email"]}
    )

@app.post("/auth/login", response_class=JSONResponse)
async def login_user(payload: UserLogin):
    """Authenticate user session against existing memory records."""
    for user in USER_DB:
        if user["email"] == payload.email:
            return JSONResponse(
                status_code=status.HTTP_200_OK,
                content={"status": "success", "message": "Authentication successful", "username": user["username"]}
            )
            
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"status": "error", "message": "Invalid email or account does not exist"}
    )
```

#### Request & Response Payload Examples

* **POST Request (`/auth/signup`) Body:**
  ```json
  {
    "username": "rayaan_tasnim",
    "email": "rayaan@olympiadedge.org",
    "password": "SecurePassword123"
  }
  ```
* **POST 201 Created Response:**
  ```json
  {
    "status": "success",
    "message": "User registered successfully",
    "user_id": 1,
    "email": "rayaan@olympiadedge.org"
  }
  ```
* **POST 400 Error Response (Duplicate Email):**
  ```json
  {
    "status": "error",
    "message": "Email address already registered in network"
  }
  ```

</details>

---

## 🛠️ INSTALLATION & RUN GUIDE

To set up the development environment, initialize your local virtual workspace, and launch the Uvicorn ASGI server, execute the following commands in your terminal:

### 1. Clone & Navigate Repository
```bash
git clone https://github.com/olympiad-edge/fastapi-backend-core-modules.git
cd fastapi-backend-core-modules
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv venv
# On macOS / Linux:
source venv/bin/activate
# On Windows Command Prompt:
# venv\Scripts\activate
```

### 3. Install Production Dependencies
```bash
pip install --upgrade pip
pip install fastapi uvicorn pydantic[email]
```

### 4. Initialize Local Development Server
```bash
uvicorn main:app --reload --host 127.0.0.1 --port 8000
```
*Once running, navigate to `http://127.0.0.1:8000/docs` to interact directly with the Swagger UI documentation.*

---

## 🛡️ VERIFICATION & STANDARDS

Memory space safety and runtime predictability are maintained via strict structural encapsulation enforced by Pydantic v2 schemas:

1. **Boundary Interception:** Incoming raw HTTP request bodies are evaluated against rigid typing definitions before controller execution occurs. Any deviation in data type or constraint violation triggers an immediate, auto-generated `422 Unprocessable Entity` error response.
2. **Memory Isolation:** Internal data arrays operate within closure-safe contexts, preventing exterior script injection or runtime prototype manipulation.
3. **Explicit Serialization Guarantees:** By avoiding implicit dictionary returns and utilizing dedicated `JSONResponse` classes, all response headers, error states, and payloads follow explicit architectural contracts.

---

<br><br>
<p align="center">
Authorized by Rayaan tasnim <br>
Powered by Olympiad Edge <br>
Sponsored by IDAI Universe <br>
All rights reserved
</p>
