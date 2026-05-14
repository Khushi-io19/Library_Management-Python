from LIB_SERVICES.login_service import admin_login

from LIB_SERVICES.book_service import (
    add_book,
    view_books,
    search_book,
    update_book,
    delete_book
)

from LIB_SERVICES.student_service import (
    add_student,
    view_students,
    search_student
)

from LIB_SERVICES.issue_service import (
    issue_book,
    view_issued_books
)

from LIB_SERVICES.return_service import return_book

from LIB_SERVICES.statistics_service import show_statistics


# ================= BOOK MENU =================

def book_menu():

    while True:

        print("""

========== BOOK MANAGEMENT ==========

1. Add Book
2. View Books
3. Search Book
4. Update Book
5. Delete Book
6. View Issued Books
7. Back

""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            update_book()

        elif choice == "5":
            delete_book()

        elif choice == "6":
            view_issued_books()

        elif choice == "7":
            break

        else:
            print("\n❌ Invalid Choice!")


# ================= STUDENT MENU =================

def student_menu():

    while True:

        print("""

========== STUDENT MANAGEMENT ==========

1. Add Student
2. View Students
3. Search Student
4. Back

""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            break

        else:
            print("\n❌ Invalid Choice!")


# ================= MAIN MENU =================

def menu():

    while True:

        print("""

========================================
📚 SMART LIBRARY MANAGEMENT SYSTEM
========================================

1. Book Management
2. Student Management
3. Issue Book
4. Return Book
5. Statistics
6. Exit

""")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            book_menu()

        elif choice == "2":
            student_menu()

        elif choice == "3":
            issue_book()

        elif choice == "4":
            return_book()

        elif choice == "5":
            show_statistics()

        elif choice == "6":
            print("\n👋 Exiting Program...")
            break

        else:
            print("\n❌ Invalid Choice!")


# ================= START PROGRAM =================

if admin_login():
    menu()