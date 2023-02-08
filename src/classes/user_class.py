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

    def login(self):
        """
        Function for user login process
        """
        self.username = input("Username: ")
        password = input("Password: ")
        if self.users_col.find_one(
            {"$and": [{"username": self.username}, {"password": password}]}
        ):
            print("Login is succesfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def register(self):
        """
        Function for user register process
        """
        username = input("\nUsername: ")
        password = input("Password: ")

        self.users_col.insert_one(
            {"username": username, "password": password, "occupied_books": [-1]}
        )
        print("Sign Up Successfull")

    def operations(self):
        """
        Function for user library actions
        """

        book = Book(self.users_col, self.books_col, self.username)

        while 1:
            print(
                "\n1. Search books\n2. Reserve a book \n3. Occupy a book\n4. Return a book \n5. Log out"
            )

            try:
                user_action = int(input("Choose an option for continue: "))
            except:
                print("Invalid input!")
                continue
            if user_action == 1:
                book.search()
            elif user_action == 2:
                book.reserve()
            elif user_action == 3:
                book.occupy()
            elif user_action == 4:
                book.return_()
            elif user_action == 5:
                print("Successfully logged out.")
                break
            else:
                print("Invalid input!")
            input("\nPress enter to continue: ")
        return 0
