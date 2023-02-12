"""
Module for library admin (librarian) operations
"""

from classes.book_class import Book


class Librarian:
    """Class for librarian operations"""

    def __init__(self, librarian_col, books_col, users_col):
        self.librarian_col = librarian_col
        self.books_col = books_col
        self.users_col = users_col

    def login(self):
        """
        Function for librarian login process
        """
        librarian_password = input("Password: ")

        if librarian_password == self.librarian_col.find_one()["librarian_password"]:
            return {"status": 1, "message": "Login is successful."}
        else:
            return {"status": 0, "message": "Login is not successful."}

    def operations(self, librarian_action):
        """
        Function for librarian actions
        """
        book = Book(self.users_col, self.books_col)

        if librarian_action == 1:
            return book.show()

        elif librarian_action == 2:
            msg = []
            try:
                for data in self.users_col.find({}, {"_id": 0}):
                    msg.append(data)
                return {"status": 1, "message": "All the users are listed", "data": msg}
            except:
                return {
                    "status": 0,
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
                return {"status": 99, "message": "Invalid input!"}
            return book.add(
                title, author, subject_category, publication_date, physical_address
            )

        elif librarian_action == 4:
            try:
                delete_id = int(input("ID of the book: "))
            except:
                return {"status": 99, "message": "Invalid input!"}
            return book.remove(delete_id)
        elif librarian_action == 5:
            return {"status": 100, "message": "Logged out"}
        else:
            return {"status": 99, "message": "Invalid input!"}
