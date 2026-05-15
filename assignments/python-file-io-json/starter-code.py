from __future__ import annotations
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

BOOKS_FILE = Path("books.json")
Book = Dict[str, Any]


def load_books(file_path: Path = BOOKS_FILE) -> List[Book]:
    """Load books from a JSON file and return a list of book dictionaries."""
    if not file_path.exists():
        return []
    with file_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books: List[Book], file_path: Path = BOOKS_FILE) -> None:
    """Save the list of books to a JSON file."""
    with file_path.open("w", encoding="utf-8") as file:
        json.dump(books, file, indent=2)


def find_book(book_id: int, books: List[Book]) -> Optional[Book]:
    """Return a book by ID or None if the book is not found."""
    return next((book for book in books if book.get("id") == book_id), None)


def add_book(new_book: Book, books: List[Book]) -> List[Book]:
    """Add a new book to the list and return the updated list."""
    if find_book(new_book.get("id"), books) is not None:
        raise ValueError("A book with this ID already exists.")
    books.append(new_book)
    return books


def update_book(book_id: int, updated_fields: Book, books: List[Book]) -> List[Book]:
    """Update a book's fields and return the updated list."""
    book = find_book(book_id, books)
    if book is None:
        raise ValueError("Book not found")
    book.update(updated_fields)
    return books


def delete_book(book_id: int, books: List[Book]) -> List[Book]:
    """Delete a book by ID and return the updated list."""
    return [book for book in books if book.get("id") != book_id]


def main() -> None:
    books = load_books()
    print("Loaded books:")
    print(json.dumps(books, indent=2))

    new_book = {
        "id": 3,
        "title": "Python File I/O",
        "author": "Mergington Teacher",
        "year": 2026,
    }

    books = add_book(new_book, books)
    save_books(books)
    print("\nAdded a new book and saved books.json.")


if __name__ == "__main__":
    main()
