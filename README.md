📘 Smart Library Management System

A console-based Library Management System developed using Core Python.
This project helps manage books, students, issue/return operations, fine calculation, and library statistics using OOP, JSON file handling, and modular programming.

🚀 Features

🔐 Login System
Admin authentication
Username & password validation

📚 Book Management
Add Book
View Books
Search Book
Update Book
Delete Book

👤 Student Management
Add Student
View Students
Search Student

📕 Library Operations
Issue Book
Return Book
View Issued Books
Automatic Quantity Tracking

💰 Fine Calculation
Calculates late return fine
₹10 fine per day after 7 days

📊 Statistics
Total Books
Total Students
Total Issued Books
Available Books Count

🛠 Technologies Used
Python
JSON
OOP (Object-Oriented Programming)
Modular Programming
Datetime Module

📁 Project Structure

LIBRARY_MANAGEMENT/
│
├── main.py
│
├── LIB_MODELS/
│   ├── book.py
│   ├── student.py
│   └── issue.py
│
├── LIB_SERVICES/
│   ├── login_service.py
│   ├── book_service.py
│   ├── student_service.py
│   ├── issue_service.py
│   ├── return_service.py
│   └── statistics_service.py
│
├── LIB_UTILS/
│   ├── file_handler.py
│   ├── validation.py
│   └── fine_calculator.py
│
└── LIB_DATA/
    ├── admin.json
    ├── books.json
    ├── students.json
    └── issued_books.json

▶ How To Run

Step 1
Open terminal in project folder.

Step 2
Run:
python main.py

🔑 Login Credentials
Username : admin
Password : 1234

📦 Sample Book Record
{
    "book_id": "B01",
    "title": "Python Basics",
    "author": "John Smith",
    "quantity": 5
}

🎯 Concepts Used
Classes & Objects
Functions
Loops & Conditions
JSON File Handling
Exception Handling
Date & Time Handling
Modular Programming

📌 Project Objective
The objective of this project is to automate and simplify library management operations while demonstrating Core Python concepts through a real-world application.

👨‍💻 Developed By
Khushi aka Yeji aka Jiaxiaozi✨
