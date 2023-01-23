
class Librarian:
    def __init__(self, librarian_col,books_col, users_col):
            self.librarian_col = librarian_col
            self.books_col = books_col
            self.users_col = users_col

    def librarian_login(self):
        librarian_password = input("Password: ")

        if librarian_password == self.librarian_col.find_one()["librarian_password"]:
            print("Login is successfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def librarian_operations(self):
        while 1:
            print("\n1. Show All Books\n2. Show All Users\n3. Add a Book\n4. Remove a Book\n5. Log Out")
            librarian_action = int(input("Choose an option for continue: "))
            if librarian_action == 1:
                for data in self.books_col.find({},{"_id":0}):
                    print(data)
            elif librarian_action == 2:
                for data in self.users_col.find({},{"_id":0}):
                    print(data)
            elif librarian_action == 3:
                new_title = input("Title of the new book: ")
                new_author = input("Author of the new book: ")
                id_ = self.books_col.find().sort("id",-1)
                new_id = id_[0]["id"]+1
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
                "book_state": "Free"
                }
                self.books_col.insert_one(new_book)
                print("The new book is added.")
            elif librarian_action == 4:
                delete_id = int(input("ID of the book: "))
                self.books_col.delete_one({"id":delete_id})
                print("The book is deleted.")

            elif librarian_action == 5:
                print("Logged out.")
                return 1
            else:
                print("Invalid input. Try Again.")