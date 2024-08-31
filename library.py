class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book["isbn"]] = book
