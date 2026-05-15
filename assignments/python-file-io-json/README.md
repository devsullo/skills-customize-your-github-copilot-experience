# 📘 Assignment: Python File I/O and JSON Data

## 🎯 Objective

Learn how to read, write, and update JSON data files in Python. Practice managing file-based data, handling missing files, and saving changes back to disk.

## 📝 Tasks

### 🛠️ Load and inspect JSON data

#### Description
Use Python file I/O to read a list of books from `books.json` and load it into your program.

#### Requirements
Completed program should:
- Open `books.json` in read mode
- Parse the JSON data into Python objects
- Return an empty list when the file does not exist
- Print the loaded book records to the console

### 🛠️ Add and save new records

#### Description
Create new book records and save them back to the JSON file.

#### Requirements
Completed program should:
- Add a new book record with `id`, `title`, `author`, and `year`
- Save the updated list back to `books.json`
- Preserve the JSON file format so it can be loaded again

### 🛠️ Update and delete existing records

#### Description
Modify an existing book entry and remove a book by ID.

#### Requirements
Completed program should:
- Find a book by its `id`
- Update the book's details and save the change
- Delete a book by ID and save the updated list
- Handle attempts to edit or delete a missing book gracefully

## ✅ Bonus Challenge

- Add validation to ensure `year` is a positive integer
- Handle invalid JSON in `books.json` with a clear error message
- Write the JSON file with indentation for readability

## 📤 Submission

- Submit `starter-code.py`
- Keep `books.json` in the assignment folder as sample data
- Include this `README.md` with your completed assignment
