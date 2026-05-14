import json


# ================= READ JSON =================


def read_json(filename):

    try:

        with open(filename, "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []


# ================= WRITE JSON =================


def write_json(filename, data):

    with open(filename, "w") as file:
        json.dump(data, file, indent=4)