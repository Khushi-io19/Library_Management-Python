from datetime import datetime


class Issue:

    def __init__(self, student_id, book_id):

        self.student_id = student_id
        self.book_id = book_id
        self.issue_date = datetime.now().strftime("%Y-%m-%d")

    def to_dict(self):

        return {
            "student_id": self.student_id,
            "book_id": self.book_id,
            "issue_date": self.issue_date
        }