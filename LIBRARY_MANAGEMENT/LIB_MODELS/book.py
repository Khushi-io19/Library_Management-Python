class Book:

    def __init__(self, book_id, title, author, quantity):

        self.book_id = book_id
        self.title = title
        self.author = author
        self.quantity = quantity

    def to_dict(self):

        return {
            "book_id": self.book_id,
            "title": self.title,
            "author": self.author,
            "quantity": self.quantity
        }