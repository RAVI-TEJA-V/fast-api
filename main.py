import email
from operator import gt
from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

from api import users,courses,sections


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

app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)


