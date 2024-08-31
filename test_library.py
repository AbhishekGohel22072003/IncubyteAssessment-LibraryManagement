import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        library.add_book(book)
        self.assertIn(book["isbn"], library.books)

    def test_add_book_with_missing_fields(self):
        library = Library()
        incomplete_book = {"isbn": "1", "title": "My Book"}
        with self.assertRaises(ValueError):
            library.add_book(incomplete_book)

    def test_add_book_with_duplicate_isbn(self):
        library = Library()
        book = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        library.add_book(book)
        with self.assertRaises(ValueError):
            library.add_book(book)

    def test_borrow_book(self):
        library = Library()
        book = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        library.add_book(book)
        result = library.borrow_book("1")
        self.assertEqual(result, "Book borrowed")
        self.assertNotIn("1", library.books)

    def test_borrow_nonexistent_book(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.borrow_book("nonexistent_isbn")
            
    def test_return_book(self):
        library = Library()
        book = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        library.add_book(book)
        library.borrow_book("1")
        result = library.return_book("1")
        self.assertEqual(result, "Book returned")
        self.assertIn("1", library.books)

    def test_return_nonexistent_book(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.return_book("nonexistent_isbn")

    def test_view_available_books(self):
        library = Library()
        book1 = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        book2 = {"isbn": "2", "title": "Another Book", "author": "Author", "year": 2023}
        library.add_book(book1)
        library.add_book(book2)
        available_books = library.view_available_books()
        self.assertEqual(available_books, {"1": book1, "2": book2})

    def test_view_no_available_books(self):
        library = Library()
        with self.assertRaises(ValueError):
            library.view_available_books()

if __name__ == '__main__':
    unittest.main()
