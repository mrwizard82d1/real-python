from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


books = [
    {"id": 1,
     "title": "Python Basics",
     "author": "Real P.",
     "pages": 635},
    {"id": 2,
     "title": "Breaking the Rules",
     "author": "Stephen G.",
     "pages": 99}
]


class Book(BaseModel):
    title: str
    author: str
    pages: int


@app.get("/books")
def get_books(limit: int | None = None):
    """Get all books, optionally limited by `limit`."""
    if limit:
        return {"books": books[:limit]}

    return {"books" : books}
