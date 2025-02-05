class Book:
    '''
    A book will have a title, an author and an isbn (think of it as a UUID).
    For any given book, it should be noted who has checked this copy of the book out. Hence checked_out_by.
    The type checked_out_by is up to you, so long as it meets the requirements listed.
    '''
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.checked_out_by = None

    def check_out(self, borrower: Borrower):
        pass

    def check_in(self):
        pass


class Author:
    def __init__(self, name: str):
        self.name = name

class Borrower:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.books_checked_out = []

class Library:
    '''
    Library is initially set to hold a collection of books, borrowers and authors.
    It is initiallized as a list. It's up to you to decide if it should remain that way.
    '''
    def __init__(self):
        self.books = []
        self.borrowers = []
        self.authors = []

    def add_book(self, title: str, author_name: str, isbn: str):
        pass

    def add_borrower(self, name: str, email: str):
        pass

    def find_or_create_author(self, author_name: str):
        pass
        
    def find_book(self, book_title: str):
        pass

    def find_borrower(self, borrower_email: str):
        pass
    
    def get_stock(self, book_title: str) -> int:
        pass

    def check_out_book(self, book_title: str, borrower_email: str):
        pass

    def check_in_book(self, book: Book):
        pass