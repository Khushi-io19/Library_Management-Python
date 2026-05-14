from LIB_UTILS.file_handler import read_json
from LIB_UTILS.validation import is_empty

ADMIN_FILE = "LIB_DATA/admin.json"


# ================= ADMIN LOGIN =================


def admin_login():

    print("\n========== ADMIN LOGIN ==========")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if is_empty(username) or is_empty(password):
        print("\n❌ Fields Cannot Be Empty!")
        return False

    admins = read_json(ADMIN_FILE)

    for admin in admins:

        if (
            admin["username"] == username
            and admin["password"] == password
        ):

            print("\n✅ Login Successful!")
            return True

    print("\n❌ Invalid Username or Password!")
    return False