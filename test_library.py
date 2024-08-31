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

if __name__ == '__main__':
    unittest.main()
