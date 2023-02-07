"""
Module for all book operations
"""


class Book:
    """Class for all book operations"""

    def __init__(self, users_col, books_col, username=""):
        self.books_col = books_col
        self.users_col = users_col
        self.username = username

    def search(self):
        """
        Function for book searching in library database
        """
        search = BookSearch(self.books_col)

        print(
            "\n1. Search books by title\n2. Search books by author\n3. Search books by subject category\n4. Search books by publication date"
        )
        try:
            user_action = int(input("Choose an option for continue: "))
        except:
            print("Invalid input!")
            return 0
        if user_action == 1:
            search.title()
        elif user_action == 2:
            search.author()
        elif user_action == 3:
            search.subject_category()
        elif user_action == 4:
            search.publication_date()
        else:
            print("Invalid input!")

    def reserve(self):
        """
        Function for book reserving from library
        """
        _id = int(input("\nInput ID of the book: "))

        target_book = None
        target_book = self.books_col.find_one({"id": _id})
        if target_book:
            if target_book["book_state"] == ("Reserved" or "Occupied"):
                print("The book is not free.")
            else:
                _filter = {"id": _id}
                _newvalues = {"$set": {"book_state": "Reserved"}}
                self.books_col.update_one(_filter, _newvalues)
                print("The book is reserved successfully.")
        else:
            print("The book not found.")

    def occupy(self):
        """
        Function for book occupying
        """
        _id = int(input("\nInput ID of the book: "))

        target_book = None
        target_book = self.books_col.find_one({"id": _id})
        if target_book:
            if target_book["book_state"] == "Occupied":
                print("The book is not free.")
            else:
                user_occupied_books = (
                    self.users_col.find_one({"username": self.username})
                )["occupied_books"]

                if len(user_occupied_books) < 6:
                    user_occupied_books.append(_id)
                    user_filter = {"username": self.username}
                    user_newvalue = {"$set": {"occupied_books": user_occupied_books}}
                    self.users_col.update_one(user_filter, user_newvalue)

                    book_filter = {"id": _id}
                    book_newvalue = {"$set": {"book_state": "Occupied"}}
                    self.books_col.update_one(book_filter, book_newvalue)
                    print("The book is occupied.")
                else:
                    print("Maximum number of occupied book cannot be higher than 5!")
        else:
            print("The book not found.")

    def return_(self):
        """
        Function for book returning
        """
        _id = int(input("\nInput ID of the book: "))

        target_book = None
        target_book = self.books_col.find_one({"id": _id})

        if target_book:
            if target_book["book_state"] == "Occupied":
                user_occupied_books = (
                    self.users_col.find_one({"username": self.username})
                )["occupied_books"]

                if _id in user_occupied_books:
                    user_occupied_books.remove(_id)
                    user_filter = {"username": self.username}
                    user_newvalue = {"$set": {"occupied_books": user_occupied_books}}
                    self.users_col.update_one(user_filter, user_newvalue)

                    book_filter = {"id": _id}
                    book_newvalue = {"$set": {"book_state": "Free"}}
                    self.books_col.update_one(book_filter, book_newvalue)
                    print("The book is returned succesfully.")
                else:
                    print("The book has not occupied by current user.")
            else:
                print("The book is already free.")
        else:
            print("The book not found.")

    def show(self):
        """
        Function for monitoring all books in database
        """
        for data in self.books_col.find({}, {"_id": 0}):
            print(data)

    def add(self):
        """
        Function for add new books to database
        """
        new_title = input("Title of the new book: ")
        new_author = input("Author of the new book: ")
        id_ = self.books_col.find().sort("id", -1)
        new_id = id_[0]["id"] + 1
        new_subject_category = input("Subject category of the new book: ")
        new_publication_date = input("Publication date of the new book: ")
        new_physical_address = input("Physical address of the new book: ")
        new_book_state = "Free"

        new_book = {
            "title": new_title,
            "id": new_id,
            "author": new_author,
            "subject_category": new_subject_category,
            "publication_date": new_publication_date,
            "physical_address": new_physical_address,
            "book_state": "Free",
        }
        self.books_col.insert_one(new_book)
        print("The new book is added.")

    def remove(self):
        """
        Function for removing books from database
        """
        delete_id = int(input("ID of the book: "))
        self.books_col.delete_one({"id": delete_id})
        print("The book is deleted.")


class BookSearch:
    """A sub class for book searching from database"""

    def __init__(self, books_col):
        self.books_col = books_col

    def title(self):
        """
        Function for searching books according to the book title
        """
        _input = input("\nInput the title: ")
        data = self.books_col.find({"title": _input}, {"_id": 0})
        _data = None
        for _data in data:
            print(_data)
        if not _data:
            print("Book does not exist.")

    def author(self):
        """
        Function for searching books according to the book author
        """
        _input = input("\nInput the author: ")
        data = self.books_col.find({"author": _input}, {"_id": 0})
        _data = None
        for _data in data:
            print(_data)
        if not _data:
            print("Book does not exist.")

    def subject_category(self):
        """
        Function for searching books according to the book subject category
        """
        _input = input("\nInput the subject: ")
        data = self.books_col.find({"subject_category": _input}, {"_id": 0})
        _data = None
        for _data in data:
            print(_data)
        if not _data:
            print("Book does not exist.")

    def publication_date(self):
        """
        Function for searching books according to the book publication date
        """
        _input = input("\nInput the publication date: ")
        data = self.books_col.find({"publication_date": _input}, {"_id": 0})
        _data = None
        for _data in data:
            print(_data)
        if not _data:
            print("Book does not exist.")
