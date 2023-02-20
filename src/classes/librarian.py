"""
Module for library admin (librarian) operations
"""

from .book import Book
from .status import Status


class Librarian:
    """Class for librarian operations"""

    def __init__(self, librarian_col, books_col, users_col):
        self.librarian_col = librarian_col
        self.books_col = books_col
        self.users_col = users_col

    def login(self, librarian_password):
        """
        Function for librarian login process

        Parameters
        ----------
        librarian_password: int, default: None
            Password of the librarian for login operation

        Returns
        -------
        dict
            Dictionary that includes "status" and "message" keys
        """

        if librarian_password == self.librarian_col.find_one()["librarian_password"]:
            return {"status": Status.Success, "message": "Login is successful."}
        else:
            return {"status": Status.Fail, "message": "Login is not successful."}

    def operations(self, librarian_action):
        """
        Function for librarian actions

        Parameters
        ----------
        librarian_action: int, default: None
            Number of librarian operation choice

        Returns
        -------
        dict
            Dictionary that includes "status", "message" and "data" (optional) keys
        """
        book = Book(self.users_col, self.books_col)

        if librarian_action == 1:
            return book.show()

        elif librarian_action == 2:
            msg = []
            try:
                for data in self.users_col.find({}, {"_id": 0}):
                    msg.append(data)
                return {
                    "status": Status.Success,
                    "message": "All the users are listed",
                    "data": msg,
                }
            except:
                return {
                    "status": Status.Fail,
                    "message": "The users could not be listed.",
                    "data": [],
                }
        elif librarian_action == 3:
            try:
                title = input("Title of the new book: ")
                author = input("Author of the new book: ")
                subject_category = input("Subject category of the new book: ")
                publication_date = input("Publication date of the new book: ")
                physical_address = input("Physical address of the new book: ")
            except:
                return {"status": Status.InvalidInput, "message": "Invalid input!"}
            return book.add(
                title, author, subject_category, publication_date, physical_address
            )

        elif librarian_action == 4:
            try:
                delete_id = int(input("ID of the book: "))
            except:
                return {"status": Status.InvalidInput, "message": "Invalid input!"}
            return book.remove(delete_id)
        elif librarian_action == 5:
            return {"status": Status.LogOut, "message": "Logged out"}
        else:
            return {"status": Status.InvalidInput, "message": "Invalid input!"}
