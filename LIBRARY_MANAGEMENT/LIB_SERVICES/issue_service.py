from LIB_MODELS.issue import Issue

from LIB_UTILS.file_handler import (
    read_json,
    write_json
)

BOOK_FILE = "LIB_DATA/books.json"
STUDENT_FILE = "LIB_DATA/students.json"
ISSUE_FILE = "LIB_DATA/issued_books.json"


# ================= ISSUE BOOK =================

def issue_book():

    print("\n========== ISSUE BOOK ==========")

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")

    students = read_json(STUDENT_FILE)

    student_found = False

    for student in students:

        if student["student_id"] == student_id:
            student_found = True
            break

    if not student_found:
        print("\n❌ Student Not Found!")
        return

    books = read_json(BOOK_FILE)

    book_found = False

    for book in books:

        if book["book_id"] == book_id:

            book_found = True

            if book["quantity"] <= 0:
                print("\n❌ Book Out Of Stock!")
                return

            book["quantity"] -= 1
            break

    if not book_found:
        print("\n❌ Book Not Found!")
        return

    write_json(BOOK_FILE, books)

    issues = read_json(ISSUE_FILE)

    new_issue = Issue(student_id, book_id)

    issues.append(new_issue.to_dict())

    write_json(ISSUE_FILE, issues)

    print("\n✅ Book Issued Successfully!")


# ================= VIEW ISSUED BOOKS =================

def view_issued_books():

    print("\n========== ISSUED BOOKS ==========")

    issues = read_json(ISSUE_FILE)

    students = read_json(STUDENT_FILE)

    books = read_json(BOOK_FILE)

    if not issues:
        print("\n❌ No Issued Books Found!")
        return

    for issue in issues:

        student_name = "Unknown"
        book_name = "Unknown"

        # ---------- FIND STUDENT NAME ----------

        for student in students:

            if student["student_id"] == issue["student_id"]:

                student_name = student["name"]
                break

        # ---------- FIND BOOK NAME ----------

        for book in books:

            if book["book_id"] == issue["book_id"]:

                book_name = book["title"]
                break

        print(f"""

Issue Details

Student ID   : {issue['student_id']}
Student Name : {student_name}

Book ID      : {issue['book_id']}
Book Name    : {book_name}

Issue Date   : {issue['issue_date']}

-----------------------------------
""")