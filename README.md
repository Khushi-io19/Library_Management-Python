📚 SMART LIBRARY MANAGEMENT SYSTEM

A console-based Library Management System built using Python and JSON. This project helps manage books, students, issuing and returning of books, fine calculation, issued records, and library statistics in an organized and efficient way.

🚀 FEATURES

✅ Admin Login System
✅ JSON Database Storage
✅ Book Management System
✅ Add / View / Search Books
✅ Update & Delete Books
✅ Student Management System
✅ Issue Book System
✅ Return Book System
✅ View Issued Books
✅ Automatic Quantity Tracking
✅ Fine Calculation System
✅ Library Statistics System
✅ Modular Programming Structure

💰 FINE CALCULATION SYSTEM

Rule	Fine
First 7 Days	No Fine
After 7 Days	₹10 Per Day

📁 PROJECT STRUCTURE

```plaintext id="d4hjpv"
library_management/
│
├── LIB_DATA/
│   ├── admin.json
│   ├── books.json
│   ├── students.json
│   └── issued_books.json
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
└── main.py
```

💾 TECHNOLOGIES USED

* Python
* JSON
* Object-Oriented Programming (OOP)
* File Handling
* Datetime Module
* Modular Programming

▶️ HOW TO RUN

Open project folder in VS Code
Open terminal
Run:

```bash id="jlwm2w"
python main.py
```

🔑 LOGIN DETAILS

```plaintext id="jzq2ow"
Username : admin
Password : 1234
```

📋 MAIN MENU

```plaintext id="l7vxmk"
1. Book Management
2. Student Management
3. Issue Book
4. Return Book
5. Statistics
6. Exit
```

📚 BOOK MANAGEMENT

* Add Book
* View Books
* Search Book
* Update Book
* Delete Book
* View Issued Books

👤 STUDENT MANAGEMENT

* Add Student
* View Students
* Search Student

📕 ISSUE & RETURN SYSTEM

The system automatically:

* Checks student records
* Checks book availability
* Reduces quantity after issuing
* Increases quantity after return
* Saves issued records
* Calculates fine automatically

📊 STATISTICS SYSTEM

Displays:

* Total Books
* Total Students
* Total Issued Books
* Available Books Count

📦 DATA STORAGE

All data is stored using JSON files:

* admin.json
* books.json
* students.json
* issued_books.json

🌟 FUTURE IMPROVEMENTS

* Admin Dashboard
* GUI Version
* SQLite Database Integration
* Barcode Scanner
* Book Reservation System
* Export Reports
* Email Notifications

👨‍💻 AUTHOR

Developed by Khushi ✨✨
