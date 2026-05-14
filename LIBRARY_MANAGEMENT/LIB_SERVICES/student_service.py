from LIB_MODELS.student import Student

from LIB_UTILS.file_handler import (
    read_json,
    write_json
)

STUDENT_FILE = "LIB_DATA/students.json"


# ================= ADD STUDENT =================

def add_student():

    print("\n========== ADD STUDENT ==========")

    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")

    students = read_json(STUDENT_FILE)

    for student in students:

        if student["student_id"] == student_id:
            print("\n❌ Student ID Already Exists!")
            return

    new_student = Student(student_id, name)

    students.append(new_student.to_dict())

    write_json(STUDENT_FILE, students)

    print("\n✅ Student Added Successfully!")


# ================= VIEW STUDENTS =================

def view_students():

    print("\n========== ALL STUDENTS ==========")

    students = read_json(STUDENT_FILE)

    if not students:
        print("\n❌ No Students Found!")
        return

    for student in students:

        print(f"""
👤 Student ID   : {student['student_id']}
📝 Name         : {student['name']}
--------------------------------
""")


# ================= SEARCH STUDENT =================

def search_student():

    keyword = input("\nEnter Student Name: ").lower()

    students = read_json(STUDENT_FILE)

    found = False

    for student in students:

        if keyword in student["name"].lower():

            found = True

            print(f"""
👤 Student ID   : {student['student_id']}
📝 Name         : {student['name']}
--------------------------------
""")

    if not found:
        print("\n❌ Student Not Found!")