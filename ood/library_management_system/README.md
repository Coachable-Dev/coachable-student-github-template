# Library Management System 



Passing score: 100%



Extra Credit: 10%





Context: The goal is to create a management system for a library. The management system should be able to track the inventory of books that go in and out





Requirements (50%):

- The System should track books that are added to the library.
- Books that are added to the library can be assumed to be unique.
- Borrowers should be able to checkout books. When books are already checked out, they cannot be taken and/or checkout again.
```
    def check_out_book(self, book_title, borrower_email):
        # If the book is available and the borrower is valid, return the book.
        # Else, return nothing.
```

- Borrowers should be able to check in the books that they have borrowed. This mean that they have returned the book back to the library, and will be available for others to borrow. Borrowers should not be able to return books if the library doesn't own them.

```
    def check_in_book(self, book):
        # If the book belongs to the library, and the borrower of the book is registered to the library, add it back in, and return True
        # Else, return False
```

- There should be helper functions that aid with the main two functions/APIs stated above. The first of which is find_book()

```
    def find_book(self, book_title):
        # If the book belongs to the library, return the book object
        # Else, return nothing.
```

- Another helper function that should help is find_borrower()

```
    def find_borrower(self, borrower_email):
        # If the borrower is registered with the library, return the borrower info
        # Else, return nothing.
```

- We now need to add and register borrowers, and books, with the consideration for future plans to flush out information about the authors. This mean, that everytime we add a book, we should also register the author, if we haven't seen them before. To do so, we need a function like find_or_create_author()

```
    def find_or_create_author(self, author_name):
        # If the author is registered with the library, return the author info
        # Else, register the author with the library, then return the author.
```

- Likewise, we also need add_book() and add_borrower(), to add and register books and borrowers.

```
    def add_book(self, title, author_name, isbn):
        # Find the author, if not register the author if the author isn't already registered.
        # Register the book to the library
  
    def add_borrower(self, name, email):
        # Register the borrower to the library
```

Updated Requirements (40%):

- The library should now support multiple copies of the same book.
- Authors should now have information on all the books that they wrote and that are present in the library.
- Borrowers cannot have more than 3 books that have been checkout by them, and we should also know what books they have checked out.
- Modify the code accordingly to fit these requirements.




Implementaion tips:

- Disclaimer: these are tips, and not complete implementation details. You will need to reason about how best to implement these given the requirements above, and with accordance to the unit test provided. You are free to add more helper functions and objects as neccessary, so long as it passess the unit tests (our functional requirements.).
- Our Author class should now account for all the books that they've written that exists in the library. Create the member functions and instance attributes accordingly.
- For add_book(), if the book added has the same title as an existing book, we now expect to have two copies of the same book. What data structure changes and logic changes will be up to you (that's what we'll be grading :) ).
- Furthermore, add_book() should also add the new book to the author if the author already exists. If not you would register the author and the author's new book to both the library and the collection of the author's work (a data strucutre instance attribute that you will create for the Author class.)
- Note: we will now expect in_stock() to be implemented, as we will support multiple copies of each book.

```
    def in_stock(self, book_title):
        # If the book belongs to the library and the still exists copies of it in the library, return the current stock
        # Else, return 0
```

- checkout_book() should now accomodate the change above. I.e. it should check to see if the book is in stock and if the borrower's limit hasn't been reached, prior to checking out the book.
- Since the borrowers now have a maximum amount of books to checkout, and we need to know what books they checked out. The Borrower class should then be updated accordingly with new member functions and instance attributes.
- checkin_book() should now also accomodate any changes to the above. Figure out what changed in checkout_book() and modify the logic and checks accordingly.




Structure (10%):

We will be manually going through your code. If the structure of the code holds true to basic OOP (Object-Oriented Principles), we will give a passing score here.





What we're NOT looking for:

1. is comprehensive OOP, i.e. polymorphism, abstraction, inheritance, and comprehension.
2. Extensive use of complex algorithms.
3. Extensive use of complex data structures and objects.




What we are looking for:

1. Keeping your code DRY (Don't repeat yourself). This means keeping repeat code to a minimum. It also means using helper functions to help implement functions.
2. Using Appropriate data strucutres. E.g. If data needs to be unique, then use a set(hashset) or a dictionary (hashmap), etc.
3. Good simple logic. Try to avoid using many nested and/or composite if-statements. Also, avoid using large and complex functions. Odds are, something in there can be abstracted out into its own function. You should be very weary if your functions exceed more than 30 - 40 lines, you are most certainly over complicating something.




(Bonus) Stretch Goal (10%):

Now that we have an inventory system. Libararies typically don't have multiple books in store unless a book is high in demand.



Your goal is to create a sub system such that if a book is high in demand say: ~50% of checkout attempts for the last 10 checkouts, we should increase the inventory for that book by 1.



E.g. If the last 5 of the 10 attempts from the call `check_out_book()` was for George Orwell's 1984, then we should increase the inventory for 1984's copies/inventory by 1.



While we have tests for this, we do not and will not have starter code for this. It's meant to be more vague, and how easy this is task will be is dependent on how well the structure of the code was constructed for the previous requirements, i.e. if OOD principles were utilized. Show us what you got!

