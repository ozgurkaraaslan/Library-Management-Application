"""
Module for library user operations
"""

from classes.book_class import Book


class User:
    """Class for library user operations"""
    username = ""

    def __init__(self, users_col, books_col):
        self.users_col = users_col
        self.books_col = books_col

    def login(self, username, password):
        """
        Function for user login process
        """
        self.username = username
        if self.users_col.find_one(
            {"$and": [{"username": self.username}, {"password": password}]}
        ):
            return 1
        else:
            return 0

    def register(self, username, password):
        """
        Function for user register process
        """
        try:
            self.users_col.insert_one(
                {"username": username, "password": password, "occupied_books": [-1]}
            )
            return 1
        except:
            return 0

    def operations(self, user_action):
        """
        Function for user library actions
        """

        book = Book(self.users_col, self.books_col, self.username)

        if user_action == 1:
            print(
                "\n1. Search books by title\n2. Search books by author\n3. Search books by subject category\n4. Search books by publication date"
            )
            try:
                user_action = int(input("Choose an option for continue: "))
            except:
                return 99
            return book.search(user_action)

        elif user_action == 2:
            try:
                _id = int(input("\nInput ID of the book: "))
            except:
                return 99
            return book.reserve(_id)

        elif user_action == 3:
            try:
                _id = int(input("\nInput ID of the book: "))
            except:
                return 99
            return book.occupy(_id)

        elif user_action == 4:
            try:
                _id = int(input("\nInput ID of the book: "))
            except:
                return 99
            return book.return_(_id)

        elif user_action == 5:
            return 100

        else:
            return 99
