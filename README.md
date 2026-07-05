# week5-library-system
# Library Management System

## Project Overview

Library Management System is a Python-based application developed using Object-Oriented Programming (OOP) principles. The system helps librarians manage books and members efficiently. Users can add books, register members, search books, and view library records through a menu-driven interface.

This project demonstrates the practical implementation of classes, objects, methods, constructors, and relationships between different classes in Python.

---

# Objectives

The main objectives of this project are:

* To understand Object-Oriented Programming concepts.
* To implement classes and objects in a real-world application.
* To manage books and members efficiently.
* To practice modular programming using multiple Python files.
* To create a menu-driven application using Python.

---

# Features

### Book Management

* Add new books to the library.
* Store book title, author, and ISBN.
* View all available books.
* Search books by title.

### Member Management

* Register new library members.
* Store member information.
* View all registered members.

### Library Operations

* Manage books and members using separate classes.
* Search books quickly.
* Display records in a user-friendly format.

### OOP Concepts Used

* Classes and Objects
* Constructors (`__init__`)
* Attributes
* Methods
* Encapsulation
* Object Relationships
* Modular Programming

---

# Project Structure

```text id="4u7eb5"
week5-library-system/
│
├── library_system/
│   ├── __init__.py
│   ├── book.py
│   ├── member.py
│   ├── library.py
│   └── main.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
├── requirements.txt
├── README.md
├── .gitignore
└── run.py
```

---

# Module Description

## book.py

This module contains the Book class.

Attributes:

* title
* author
* isbn
* available

Responsibilities:

* Store book information.
* Display book details.

---

## member.py

This module contains the Member class.

Attributes:

* name
* member_id
* borrowed_books

Responsibilities:

* Store member information.
* Track borrowed books.

---

## library.py

This module contains the Library class.

Responsibilities:

* Add books.
* Register members.
* Search books.
* View books.
* View members.

---

## main.py

This module provides the menu-driven user interface.

Responsibilities:

* Take user input.
* Call library functions.
* Display results.

---

# Class Structure

## Book Class

```python id="omzv6c"
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
```

Purpose:

* Represents a single book in the library.

---

## Member Class

```python id="my4e1y"
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
```

Purpose:

* Represents a library member.

---

## Library Class

```python id="oj1zc0"
class Library:
    def __init__(self):
        self.books = []
        self.members = []
```

Purpose:

* Manages all books and members.

---

# How to Run

### Step 1

Open terminal inside project folder.

### Step 2

Run the application:

```bash id="j47sjn"
python run.py
```

---

# Sample Menu

```text id="74a3p5"
==============================
LIBRARY MANAGEMENT SYSTEM
==============================
1. Add Book
2. Register Member
3. View Books
4. View Members
5. Search Book
0. Exit
```

---

# Sample Output

```text id="ccnhdc"
Book Added Successfully

Python Programming
John Smith
9781234567890
```

---
# Image 
<img width="427" height="1018" alt="Output (2)" src="https://github.com/user-attachments/assets/c2f38fa0-c00f-4f3c-9ac3-4231c382a778" />

# Advantages of the System

* Easy to use.
* Organized code structure.
* Reusable classes.
* Beginner-friendly implementation.
* Demonstrates real-world OOP concepts.

---

# Testing Performed

The following test cases were verified:

### Book Operations

* Add book
* View book
* Search book

### Member Operations

* Register member
* View members

### System Testing

* Menu navigation
* Invalid option handling
* Multiple records handling

---

# Future Improvements

The following features can be added in future versions:

* Borrow book functionality
* Return book functionality
* Due date tracking
* Fine calculation
* JSON data persistence
* Database integration
* GUI interface using Tkinter
* Web version using Flask

---

# Conclusion

The Library Management System successfully demonstrates the implementation of Object-Oriented Programming concepts in Python. The project uses classes, objects, methods, and modular programming techniques to create a practical and easy-to-use library management solution.
