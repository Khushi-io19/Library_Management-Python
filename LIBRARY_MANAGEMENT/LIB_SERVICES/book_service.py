from LIB_MODELS.book import Book

from LIB_UTILS.file_handler import (
    read_json,
    write_json
)

BOOK_FILE = "LIB_DATA/books.json"


# ================= ADD BOOK =================

def add_book():

    print("\n========== ADD BOOK ==========")

    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    quantity = int(input("Enter Quantity: "))

    books = read_json(BOOK_FILE)

    for book in books:

        if book["book_id"] == book_id:
            print("\n❌ Book ID Already Exists!")
            return

    new_book = Book(book_id, title, author, quantity)

    books.append(new_book.to_dict())

    write_json(BOOK_FILE, books)

    print("\n✅ Book Added Successfully!")


# ================= VIEW BOOKS =================

def view_books():

    print("\n========== ALL BOOKS ==========")

    books = read_json(BOOK_FILE)

    if not books:
        print("\n❌ No Books Found!")
        return

    for book in books:

        print(f"""
📘 Book ID   : {book['book_id']}
📖 Title     : {book['title']}
✍ Author    : {book['author']}
📦 Quantity  : {book['quantity']}
--------------------------------
""")


# ================= SEARCH BOOK =================

def search_book():

    keyword = input("\nEnter Book Title: ").lower()

    books = read_json(BOOK_FILE)

    found = False

    for book in books:

        if keyword in book["title"].lower():

            found = True

            print(f"""
📘 Book ID   : {book['book_id']}
📖 Title     : {book['title']}
✍ Author    : {book['author']}
📦 Quantity  : {book['quantity']}
--------------------------------
""")

    if not found:
        print("\n❌ Book Not Found!")


# ================= UPDATE BOOK =================

def update_book():

    book_id = input("\nEnter Book ID To Update: ")

    books = read_json(BOOK_FILE)

    found = False

    for book in books:

        if book["book_id"] == book_id:

            found = True

            print("\nEnter New Details")

            book["title"] = input("New Title: ")
            book["author"] = input("New Author: ")
            book["quantity"] = int(input("New Quantity: "))

            break

    if found:

        write_json(BOOK_FILE, books)

        print("\n✅ Book Updated Successfully!")

    else:
        print("\n❌ Book ID Not Found!")


# ================= DELETE BOOK =================

def delete_book():

    book_id = input("\nEnter Book ID To Delete: ")

    books = read_json(BOOK_FILE)

    updated_books = []

    found = False

    for book in books:

        if book["book_id"] == book_id:
            found = True

        else:
            updated_books.append(book)

    if found:

        write_json(BOOK_FILE, updated_books)

        print("\n✅ Book Deleted Successfully!")

    else:
        print("\n❌ Book ID Not Found!")