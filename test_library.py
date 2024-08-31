import unittest
from library import Library

class TestLibrary(unittest.TestCase):
    def test_add_book(self):
        library = Library()
        book = {"isbn": "1", "title": "My Book", "author": "Abhishek", "year": 2024}
        library.add_book(book)
        self.assertIn(book["isbn"], library.books)

if __name__ == '__main__':
    unittest.main()
