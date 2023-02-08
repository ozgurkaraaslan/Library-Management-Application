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
            print("Login is successfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def operations(self):
        """
        Function for librarian actions
        """
        book = Book(self.users_col, self.books_col)

        while 1:
            print(
                "\n1. Show All Books\n2. Show All Users\n3. Add a Book\n4. Remove a Book\n5. Log Out"
            )

            try:
                librarian_action = int(input("Choose an option for continue: "))
            except:
                print("Invalid input!")
                continue
            if librarian_action == 1:
                book.show()
            elif librarian_action == 2:
                for data in self.users_col.find({}, {"_id": 0}):
                    print(data)
            elif librarian_action == 3:
                book.add()
            elif librarian_action == 4:
                book.remove()
            elif librarian_action == 5:
                print("Logged out.")
                return 1
            else:
                print("Invalid input. Try Again.")
            input("\nPress enter to continue: ")
