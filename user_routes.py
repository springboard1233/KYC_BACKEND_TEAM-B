from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

@router.post("/signup")
def signup(user: User):
    # Save to DB
    return {"message": f"User {user.username} created successfully"}

@router.post("/login")
def login(user: User):
    # Verify with DB
    return {"message": f"User {user.username} logged in"}
