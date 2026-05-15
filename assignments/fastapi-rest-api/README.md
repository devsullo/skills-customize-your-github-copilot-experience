# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a REST API using FastAPI to manage a collection of books. Practice defining data models, implementing CRUD endpoints, and testing API behavior.

## 📝 Tasks

### 🛠️ Set up the FastAPI project

#### Description
Create a new `main.py` file and install the required packages.

#### Requirements
- Install FastAPI and Uvicorn: `pip install fastapi uvicorn`
- Create a FastAPI application instance in `main.py`
- Use Pydantic models to define API request and response schemas

### 🛠️ Define the Book data model

#### Description
Create a book schema that includes key fields and validation.

#### Requirements
- Each book should include `id`, `title`, `author`, and `year`
- Validate that `year` is a positive integer
- Use a Pydantic `BaseModel` for the book schema

### 🛠️ Implement CRUD endpoints

#### Description
Add endpoints to list, retrieve, add, update, and delete books.

#### Requirements
Completed API should provide:
- `GET /books` — list all books
- `GET /books/{id}` — return a specific book by ID
- `POST /books` — add a new book
- `PUT /books/{id}` — update an existing book by ID
- `DELETE /books/{id}` — remove a book by ID

### 🛠️ Run and test the API

#### Description
Start the FastAPI server and verify the API endpoints work.

#### Requirements
- Run the server with `uvicorn main:app --reload`
- Test each endpoint with curl, Postman, or another API client
- Confirm the API returns expected responses for valid and invalid requests

## ✅ Bonus Challenge

- Add better error handling for missing books
- Return clear error messages for invalid input
- Add a second Pydantic model for request body validation if needed

## 📤 Submission

- Submit your finished `main.py`
- Include this `README.md` with instructions for running and testing the API
