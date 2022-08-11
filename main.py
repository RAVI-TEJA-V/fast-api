import email
from operator import gt
from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

app = FastAPI(
    title=" Fast api lms",
    description="lms",
    version="0.0.1",
    contact={
        "name" : "Gwen",
        "email" : "gwen@example.com",

    },
    license_info={
        "name" : "Mit",
    },

)

users = []

class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"

@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="the id of the user you waant", gt=2),
    q : str = Query(None, max_length=5)
 ):
    
    
    return {"user":users[id], "query": q }