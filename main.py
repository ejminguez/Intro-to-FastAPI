from fastapi import FastAPI, Path
from pydantic import BaseModel, Field

app = FastAPI(
    title="User Demo API",
    description="A simple demo API showing data validation and automatic documentation",
    version="1.0.0"
)

# Define data model with validation
class User(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="User's full name")
    age: int = Field(..., ge=0, le=150, description="User's age")
    email: str = Field(..., description="User's email address")
    
    class Config:
        example = {
            "name": "Francis Reid",
            "age": 30,
            "email": "francis@example.com"
        }

@app.get("/")
def root():
    """Welcome endpoint"""
    return {"message": "Welcome to User Demo API"}

@app.post("/users/")
def create_user(user: User):
    """Create a new user with validation"""
    return {
        "status": "success",
        "message": f"User {user.name} created successfully!",
        "data": user
    }

@app.get("/users/{user_id}")
def get_user(user_id: int = Path(..., gt=0, description="The user ID")):
    """Get user by ID"""
    return {
        "user_id": user_id,
        "name": "Francis Reid",
        "age": 30,
        "email": "francis@example.com"
    }
