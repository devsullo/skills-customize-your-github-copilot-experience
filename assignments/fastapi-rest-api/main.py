# main.py - FastAPI REST API Starter Code

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# Pydantic model for Book
class Book(BaseModel):
    id: int
    title: str
    author: str
    year: int = Field(..., gt=0, description="Year must be a positive integer.")

# In-memory storage for books
books_db: List[Book] = []

@app.get("/books", response_model=List[Book])
def list_books():
    return books_db

@app.get("/books/{book_id}", response_model=Book)
def get_book(book_id: int):
    for book in books_db:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.post("/books", response_model=Book)
def add_book(book: Book):
    if any(existing.id == book.id for existing in books_db):
        raise HTTPException(status_code=400, detail="A book with this ID already exists")
    books_db.append(book)
    return book

@app.put("/books/{book_id}", response_model=Book)
def update_book(book_id: int, updated_book: Book):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            books_db[idx] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for idx, book in enumerate(books_db):
        if book.id == book_id:
            del books_db[idx]
            return {"message": "Book deleted"}
    raise HTTPException(status_code=404, detail="Book not found")
