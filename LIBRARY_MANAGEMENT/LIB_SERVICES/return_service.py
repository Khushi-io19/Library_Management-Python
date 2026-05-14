from LIB_UTILS.file_handler import (
    read_json,
    write_json
)

from LIB_UTILS.fine_calculator import calculate_fine

BOOK_FILE = "LIB_DATA/books.json"
ISSUE_FILE = "LIB_DATA/issued_books.json"


# ================= RETURN BOOK =================

def return_book():

    print("\n========== RETURN BOOK ==========")

    student_id = input("Enter Student ID: ")
    book_id = input("Enter Book ID: ")

    issues = read_json(ISSUE_FILE)

    updated_issues = []

    issue_found = False

    fine = 0

    for issue in issues:

        if (
            issue["student_id"] == student_id
            and issue["book_id"] == book_id
        ):

            issue_found = True

            fine = calculate_fine(issue["issue_date"])

        else:
            updated_issues.append(issue)

    if not issue_found:
        print("\n❌ Issue Record Not Found!")
        return

    write_json(ISSUE_FILE, updated_issues)

    books = read_json(BOOK_FILE)

    for book in books:

        if book["book_id"] == book_id:
            book["quantity"] += 1
            break

    write_json(BOOK_FILE, books)

    print("\n✅ Book Returned Successfully!")
    print(f"\n💰 Fine Amount: ₹{fine}")