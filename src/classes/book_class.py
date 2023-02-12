"""
Module for all book operations
"""


class Book:
    """Class for book operations"""

    def __init__(self, users_col, books_col, username=""):
        self.books_col = books_col
        self.users_col = users_col
        self.username = username

    def search(self, book_action):
        """
        Function for searching books in the database
        """
        search = BookSearch(self.books_col)

        if book_action == 1:
            title = input("\nInput the title: ")
            return search.title(title)

        elif book_action == 2:
            author = input("\nInput the author: ")
            return search.author(author)

        elif book_action == 3:
            subject_category = input("\nInput the subject: ")
            return search.subject_category(subject_category)

        elif book_action == 4:
            publication_date = input("\nInput the publication date: ")
            return search.publication_date(publication_date)

        else:
            return {"status": 99, "message": "Invalid input!"}

    def reserve(self, _id):
        """
        Function for book reserving from library
        """
        msg = ""

        target_book = None
        target_book = self.books_col.find_one({"id": _id})
        if target_book:
            if target_book["book_state"] == ("Reserved" or "Occupied"):
                msg = "The book is not free."
                status = 0
            else:
                _filter = {"id": _id}
                _newvalues = {"$set": {"book_state": "Reserved"}}
                self.books_col.update_one(_filter, _newvalues)
                msg = "The book is reserved successfully."
                status = 1
        else:
            msg = "The book not found."
            status = 0
        return {"status": status, "message": msg}

    def occupy(self, _id):
        """
        Function for book occupying
        """
        msg = ""

        target_book = None
        target_book = self.books_col.find_one({"id": _id})
        if target_book:
            if target_book["book_state"] == "Occupied":
                msg = "The book is not free."
                status = 0
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

                    msg = "The book is occupied successfully."
                    status = 1
                else:
                    msg = "Maximum number of occupied book cannot be higher than 5!"
                    status = 0
        else:
            msg = "The book not found."
            status = 0
        return {"status": status, "message": msg}

    def return_(self, _id):
        """
        Function for book returning
        """
        msg = ""

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
                    msg = "The book is returned succesfully."
                    status = 1
                else:
                    msg = "The book had not occupied by current user."
                    status = 0
            else:
                msg = "The book is already free."
                status = 0
        else:
            msg = "The book not found."
            status = 0
        return {"status": status, "message": msg}

    def show(self):
        """
        Function for monitoring all books in database
        """
        msg = []
        try:
            for data in self.books_col.find({}, {"_id": 0}):
                msg.append(data)
            return {"status": 1, "message": "The books are listed.", "data": msg}
        except:
            return {
                "status": 0,
                "message": "The books could not be listed.",
                "data": [],
            }

    def add(
        self,
        title,
        author,
        subject_category,
        publication_date,
        physical_address,
        book_state="Free",
    ):
        """
        Function for add new books to database
        """
        msg = ""
        id_ = self.books_col.find().sort("id", -1)
        _id = id_[0]["id"] + 1

        try:
            book = {
                "title": title,
                "id": _id,
                "author": author,
                "subject_category": subject_category,
                "publication_date": publication_date,
                "physical_address": physical_address,
                "book_state": book_state,
            }

            self.books_col.insert_one(book)

            return {"status": 1, "message": "The new book is added."}
        except:
            return {"status": 0, "message": "The new book could not be added."}

    def remove(self, delete_id):
        """
        Function for removing books from database
        """
        msg = ""
        try:
            self.books_col.delete_one({"id": delete_id})
            return {"status": 1, "message": "The book is deleted."}
        except:
            return {"status": 0, "message": "The book could not be deleted."}


class BookSearch:
    """A sub class for book searching from database"""

    def __init__(self, books_col):
        self.books_col = books_col

    def title(self, title):
        """
        Function for searching books according to the book title
        """
        msg = []
        data = self.books_col.find({"title": title}, {"_id": 0})
        _data = None

        for _data in data:
            msg.append(_data)

        if not _data:
            return {"status": 0, "message": "Book does not exist.", "data": []}
        else:
            return {"status": 0, "message": "Book exists.", "data": msg}

    def author(self, author):
        """
        Function for searching books according to the book author
        """
        msg = []
        data = self.books_col.find({"author": author}, {"_id": 0})
        _data = None

        for _data in data:
            msg.append(_data)

        if not _data:
            return {"status": 0, "message": "Book does not exist.", "data": []}
        else:
            return {"status": 1, "message": "Book exists.", "data": msg}

    def subject_category(self, subject_category):
        """
        Function for searching books according to the book subject category
        """
        msg = []

        data = self.books_col.find({"subject_category": subject_category}, {"_id": 0})
        _data = None
        for _data in data:
            msg.append(_data)

        if not _data:
            return {"status": 0, "message": "Book does not exist.", "data": []}
        else:
            return {"status": 1, "message": "Book exists.", "data": msg}

    def publication_date(self, publication_date):
        """
        Function for searching books according to the book publication date
        """
        msg = []
        data = self.books_col.find({"publication_date": publication_date}, {"_id": 0})
        _data = None
        for _data in data:
            msg.append(_data)

        if not _data:
            return {"status": 0, "message": "Book does not exist.", "data": []}
        else:
            return {"status": 1, "message": "Book exists.", "data": msg}
