from LIB_UTILS.file_handler import read_json

BOOK_FILE = "LIB_DATA/books.json"
STUDENT_FILE = "LIB_DATA/students.json"
ISSUE_FILE = "LIB_DATA/issued_books.json"


# ================= LIBRARY STATISTICS =================

def show_statistics():

    books = read_json(BOOK_FILE)
    students = read_json(STUDENT_FILE)
    issued_books = read_json(ISSUE_FILE)

    total_books = len(books)
    total_students = len(students)
    total_issued_books = len(issued_books)

    available_quantity = 0

    for book in books:
        available_quantity += book["quantity"]

    print("""
========== LIBRARY STATISTICS ==========
""")

    print(f"📚 Total Books            : {total_books}")
    print(f"👤 Total Students         : {total_students}")
    print(f"📕 Total Issued Books     : {total_issued_books}")
    print(f"📦 Available Book Count   : {available_quantity}")