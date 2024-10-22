# Library Management System in Python - Incubyte Assessment

## Introduction
This project is a Library Management System designed as an assessment of the INCUBYTE PLACEMENT DRIVE. The system was developed using Test-Driven Development (TDD) principles. The features implemented are tested, providing confidence in the software’s reliability.

## Features
- **Add Books:** 
  - Allows users to add new books to the library with validation.
  - Ensures that books with duplicate ISBNs are not added.
  - Validates that all required fields (ISBN, title, author, year) are present.
  
- **Borrow Books:** 
  - Allows users to borrow books from the library.
  - Validates that the book is available before borrowing.
  - Moves the borrowed book to a separate list to keep track of borrowed books.

- **Return Books:**
  - Allows users to return borrowed books to the library.
  - Validates that the book was indeed borrowed before accepting the return.

- **View Available Books:**
  - Allows users to view a list of all available books in the library.
  - Validates and raises an error if no books are available.

## Requirements
- **Python 3.12.2**

## Setup & Installation

### Clone the Repository
```bash
git clone https://github.com/AbhishekGohel22072003/IncubyteAssessment-LibraryManagement.git
