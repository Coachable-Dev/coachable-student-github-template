import unittest
from library import Book, Library

class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.library.add_borrower("Alice", "alice@example.com")
        self.library.add_borrower("Bob", "bob@example.com")
        self.library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-446-31078-9")
        self.library.add_book("To Kill a Mockingbird", "Harper Lee", "978-0-446-31078-9")
        self.library.add_book("1984", "George Orwell", "978-0-143-03928-8")
        self.library.add_book("Animal Farm", "George Orwell", "978-1-379-38828-7")

    def test_check_out_book(self):
        # Valid check-out
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")

        # Book already checked out
        book3 = self.library.check_out_book("The Great Gatsby", "bob@example.com")
        self.assertIsNone(book3)

        # Book not found
        book4 = self.library.check_out_book("Moby Dick", "alice@example.com")
        self.assertIsNone(book4)

        # Borrower not found
        book5 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertIsNone(book5)

    def test_check_in_book(self):
        # Valid check-in
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        status = self.library.check_in_book(book1)
        self.assertIs(status, True)
        self.assertIsNone(self.library.find_book("The Great Gatsby").checked_out_by)

        # Book not from library
        book2 = Book("Moby Dick", "Alice", "978-2-628-32749-0")
        status = self.library.check_in_book(book2)
        self.assertIs(status, False)

        # Borrower not from library
        book3 = Book("Moby Dick", "Alice", "978-2-628-32749-0")
        book3.author = "John"
        status = self.library.check_in_book(book2)
        self.assertIs(status, False)

    def test_find_book(self):
        # Book found
        book = self.library.find_book("The Great Gatsby")
        self.assertEqual(book.title, "The Great Gatsby")

        # Book not found
        book = self.library.find_book("Moby Dick")
        self.assertIsNone(book)

    def test_find_borrower(self):
        # Borrower found
        borrower = self.library.find_borrower("alice@example.com")
        self.assertEqual(borrower.name, "Alice")
        self.assertEqual(borrower.email, "alice@example.com")

        # Borrower not found
        borrower = self.library.find_borrower("charlie@example.com")
        self.assertIsNone(borrower)

    def test_find_or_create_author(self):
        # Author found
        author = self.library.find_or_create_author("F. Scott Fitzgerald")
        self.assertEqual(author.name, "F. Scott Fitzgerald")

        # Author created
        author = self.library.find_or_create_author("Ernest Hemingway")
        self.assertEqual(author.name, "Ernest Hemingway")
        self.assertEqual(len(self.library.authors), 4)  # 3 pre-existing authors + new author

    #Updated requirement tests
    def test_check_out_multiple_books(self):
        # Valid check-out multiple copies
        book2_0 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        self.assertEqual(book2_0.checked_out_by.name, "Alice")
        book2_1 = self.library.check_out_book("To Kill a Mockingbird", "bob@example.com")
        self.assertEqual(book2_1.checked_out_by.name, "Bob")

    def test_author_information(self):
        # Author books written
        self.assertEqual(self.library.authors["George Orwell"].books, set(["1984", "Animal Farm"]))

    def test_borrower_limit(self):
        # Borrower limit
        book1 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        book2 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        book3 = self.library.check_out_book("1984", "alice@example.com")
        book4 = self.library.check_out_book("Animal Farm", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        self.assertEqual(book2.checked_out_by.name, "Alice")
        self.assertEqual(book3.checked_out_by.name, "Alice")
        self.assertIsNone(book4)

    def test_comprehensive(self):
        # Comprehensive
        book1 = self.library.check_out_book("To Kill a Mockingbird", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        book2 = self.library.check_out_book("1984", "bob@example.com")
        self.assertEqual(book2.checked_out_by.name, "Bob")
        book3 = self.library.check_out_book("1984", "bob@example.com")
        self.assertIsNone(book3)
        book4 = self.library.check_out_book("Animal Farm", "bob@example.com")
        self.assertEqual(book4.checked_out_by.name, "Bob")
        book5 = self.library.check_out_book("1984", "charlie@example.com")
        self.assertIsNone(book5)
        book6 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertIsNone(book6)
        book7 = self.library.check_out_book("1984", "david@example.com")
        self.assertIsNone(book7)
        book8 = self.library.check_out_book("Animal Farm", "david@example.com")
        self.assertIsNone(book8)
        self.library.add_borrower("David", "david@example.com")
        book9 = self.library.check_out_book("To Kill a Mockingbird", "david@example.com")
        self.assertEqual(book9.checked_out_by.name, "David")
        book10 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book10.checked_out_by.name, "Alice")

    #Strecth goal tests
    def test_supply_management(self):
        # Supply management
        self.library.add_borrower("Charlie", "charlie@example.com")
        self.library.add_borrower("David", "david@example.com")

        # Simulate check-outs for a given day
        book1 = self.library.check_out_book("1984", "alice@example.com")
        self.assertEqual(book1.checked_out_by.name, "Alice")
        book2 = self.library.check_out_book("1984", "bob@example.com")
        self.assertIsNone(book2)
        book3 = self.library.check_out_book("1984", "bob@example.com")
        self.assertIsNone(book3)
        book4 = self.library.check_out_book("Animal Farm", "bob@example.com")
        self.assertEqual(book4.checked_out_by.name, "Bob")
        book5 = self.library.check_out_book("1984", "charlie@example.com")
        self.assertIsNone(book5)
        book6 = self.library.check_out_book("To Kill a Mockingbird", "charlie@example.com")
        self.assertEqual(book6.checked_out_by.name, "Charlie")
        book7 = self.library.check_out_book("1984", "david@example.com")
        self.assertIsNone(book7)
        book8 = self.library.check_out_book("Animal Farm", "david@example.com")
        self.assertIsNone(book8)
        book9 = self.library.check_out_book("To Kill a Mockingbird", "david@example.com")
        self.assertEqual(book9.checked_out_by.name, "David")
        book10 = self.library.check_out_book("The Great Gatsby", "alice@example.com")
        self.assertEqual(book10.checked_out_by.name, "Alice")

        # Simulate total inventory after check-outs
        self.library.check_in_book(book1)
        self.assertEqual(self.library.get_stock("1984"), 2)

        # Simulate edge cases
        # Just becase the history of checkouts for a given book is pass 5
        # does not mean that we need to order more copies of the book
        # In this case, we still have copies in stock, so the order should not be placed
        book11 = self.library.check_out_book("1984", "bob@example.com")
        self.assertEqual(book11.checked_out_by.name, "Bob")
        self.library.check_in_book(book11)
        self.assertEqual(self.library.get_stock("1984"), 2)



if __name__ == '__main__':
    unittest.main()