class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        required_fields = ["isbn", "title", "author", "year"]
        for field in required_fields:
            if field not in book:
                raise ValueError(f"Missing required field: {field}")

        if book["isbn"] in self.books:
            raise ValueError(f"Book with ISBN {book['isbn']} already exists.")

        self.books[book["isbn"]] = book