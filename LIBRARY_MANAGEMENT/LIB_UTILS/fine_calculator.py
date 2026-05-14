from datetime import datetime


# ================= CALCULATE FINE =================


def calculate_fine(issue_date):

    issue_date = datetime.strptime(issue_date, "%Y-%m-%d")

    current_date = datetime.now()

    days = (current_date - issue_date).days

    if days <= 7:
        return 0

    fine = (days - 7) * 10

    return fine