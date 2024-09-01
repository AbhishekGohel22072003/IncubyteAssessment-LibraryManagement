class Library:
    def __init__(self):
        self.books = {}
        self.borrowed_books = {}

    def add_book(self, book):
        required_fields = ["isbn", "title", "author", "year"]
        for field in required_fields:
            if field not in book:
                raise ValueError(f"Missing required field: {field}")

        if book["isbn"] in self.books:
            raise ValueError(f"Book with ISBN {book['isbn']} already exists.")

        self.books[book["isbn"]] = book

    def borrow_book(self, isbn):
        if isbn not in self.books:
            raise ValueError("Book not available")
        self.borrowed_books[isbn] = self.books.pop(isbn)
        return "Book borrowed"

    def return_book(self, isbn):
        if isbn not in self.borrowed_books:
            raise ValueError("Book not recognized")
        self.books[isbn] = self.borrowed_books.pop(isbn)
        return "Book returned"

    def view_available_books(self):
        if not self.books:
            raise ValueError("No books available in the library.")
        return self.books



def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("A. Add Book")
        print("V. View Available Books")
        print("B. Borrow Book")
        print("R. Return Book")
        
        # print("e. Exit")
        # This command is secret as only the Librarian can close the Library.
        
        choice = input("Enter your choice (A, V, B or R): ").upper()

        if choice == "A":
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter year of publication: ")
            try:
                book = {"isbn": isbn, "title": title, "author": author, "year": year}
                library.add_book(book)
                print(f"Book '{title}' added successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "V":
            try:
                available_books = library.view_available_books()
                for isbn, details in available_books.items():
                    print(f"{details['title']} by {details['author']} (ISBN: {isbn}, Year: {details['year']})")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "B":
            isbn = input("Enter ISBN of the book to borrow: ")
            try:
                result = library.borrow_book(isbn)
                print(result)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "R":
            isbn = input("Enter ISBN of the book to return: ")
            try:
                result = library.return_book(isbn)
                print(result)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "E":
            print("Exiting the Library Management System.")
            break

        else:
            print("Invalid choice. Please enter a A, V, B or R.")


if __name__ == "__main__":
    main()