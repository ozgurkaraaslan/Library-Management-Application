class User:
    username = ""

    def __init__(self, users_col, books_col):
            self.users_col = users_col
            self.books_col = books_col
    def user_login(self):
        self.username = input("Username: ")
        password = input("Password: ")
        if self.users_col.find_one({"$and": [{"username": self.username}, {"password": password}]}):
            print("Login is succesfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def user_register(self):
        username = input("\nUsername: ")
        password = input("Password: ")

        self.users_col.insert_one({
                    "username": username,
                    "password": password,
                    "occupied_books": [-1]
                })
        print("Sign Up Successfull")
    def user_operations(self):
        while 1:
            print("\n1. Search books\n2. Reserve a book \n3. Occupy a book\n4. Return a book \n5. Log out")
            user_action = int(input("Choose an option for continue: "))
            if user_action == 1:
                print("\n1. Search books by title\n2. Search books by author\n3. Search books by subject category\n4. Search books by publication date")
                user_action = int(input("Choose an option for continue: "))
                if user_action == 1:
                    _input = input("\nInput the title: ")
                    data = self.books_col.find({"title":_input},{"_id":0})
                    _data = None
                    for _data in data:
                        print(_data)
                    if not _data:
                        print("Book does not exist.")
                    
                elif user_action == 2:
                    _input = input("\nInput the author: ")
                    data = self.books_col.find({"author":_input},{"_id":0})
                    _data = None
                    for _data in data:
                        print(_data)
                    if not _data:
                        print("Book does not exist.")
                elif user_action == 3:
                    _input = input("\nInput the subject: ")
                    data = self.books_col.find({"subject_category":_input},{"_id":0})
                    _data = None
                    for _data in data:
                        print(_data)
                    if not _data:
                        print("Book does not exist.")
                elif user_action == 4:
                    _input = input("\nInput the publication date: ")
                    data = self.books_col.find({"publication_date":_input},{"_id":0})
                    _data = None
                    for _data in data:
                        print(_data)
                    if not _data:
                        print("Book does not exist.")
            elif user_action == 2:
                _id = int(input("\nInput ID of the book: "))

                target_book = None
                target_book = self.books_col.find_one({"id":_id})
                if target_book:
                    if target_book["book_state"] == ("Reserved" or "Occupied"):
                        print("The book is not free.")
                    else:
                        _filter = { 'id': _id }
                        _newvalues = { "$set": { 'book_state': "Reserved" } }
                        self.books_col.update_one(_filter, _newvalues)
                        print("The book is reserved successfully.")
                else:
                    print("The book not found.")

            elif user_action == 3:
                _id = int(input("\nInput ID of the book: "))

                target_book = None
                target_book = self.books_col.find_one({"id":_id})
                if target_book:
                    if target_book["book_state"] == "Occupied":
                        print("The book is not free.")
                    else:
                        user_occupied_books = (self.users_col.find_one({"username": self.username}))["occupied_books"]

                        if len(user_occupied_books) < 6:
                            user_occupied_books.append(_id) 
                            user_filter = { 'username': self.username }
                            user_newvalue = { "$set": { 'occupied_books': user_occupied_books } }
                            self.users_col.update_one(user_filter, user_newvalue)

                            book_filter = { 'id': _id }
                            book_newvalue = { "$set": { 'book_state': "Occupied" } }
                            self.books_col.update_one(book_filter, book_newvalue)
                            print("The book is occupied.")
                        else:
                            print("Maximum number of occupied book cannot be higher than 5!")
        
                else:
                    print("The book not found.")
            elif user_action == 4:
                _id = int(input("\nInput ID of the book: "))

                target_book = None
                target_book = self.books_col.find_one({"id":_id})

                if target_book:
                    if target_book["book_state"] == "Occupied":
                        user_occupied_books = (self.users_col.find_one({"username": self.username}))["occupied_books"]

                        if _id in user_occupied_books:
                            user_occupied_books.remove(_id) 
                            user_filter = { 'username': self.username }
                            user_newvalue = { "$set": { 'occupied_books': user_occupied_books } }
                            self.users_col.update_one(user_filter, user_newvalue)

                            book_filter = { 'id': _id }
                            book_newvalue = { "$set": { 'book_state': "Free" } }
                            self.books_col.update_one(book_filter, book_newvalue)                          
                            print("The book is returned succesfully.")
                        else:
                            print("The book has not occupied by current user.")
                        
                    else:
                        print("The book is already free.")
                        
                else:
                    print("The book not found.")
            elif user_action == 5:
                print("Successfully logged out.")
                break
            input("\nPress enter to continue: ")
        return 0