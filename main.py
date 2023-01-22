import json
import pymongo

username = "rebelkrone"
password = "JqlXmO7xuMhkDAoM"

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]
librarian_col = db["librarian"]

print("Welcome to the Library Management System.")
print('''
1. User Operations
2. Librarian Operations''')

class User:
    def __init__(self, users_col):
            self.users_col = users_col

    def user_login(self):
        username = input("Username: ")
        password = input("Password: ")

        if self.users_col.find_one({"$and": [{"username": username}, {"password": password}]}):
            print("Login is succesfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def user_register(self):
        username = input("Username: ")
        password = input("Password: ")

        self.users_col.insert_one({
                    "username": username,
                    "password": password,
                    "occupied_books": []
                })
        print("Sign Up Successfull")
    def user_operations(self):
        print('''
1. Show Books
2. Show Users
3. Librarian Logout''')
        #librarian_action = int(input("Choose an option for continue: "))

class Librarian:
    def __init__(self, librarian_col):
            self.librarian_col = librarian_col

    def librarian_login(self):
        librarian_password = input("Password: ")

        if librarian_password == self.librarian_col.find_one()["librarian_password"]:
            print("Login is successfull.")
            return 1
        else:
            print("Login is not successfull!")
            return 0

    def librarian_operations(self):
        print('''
1. Show Books
2. Show Users
3. Librarian Logout''')
        librarian_action = int(input("Choose an option for continue: "))

        if librarian_action == 3:
            print("Logged out.")
            return 1

while 1:
    input_type = int(input("Choose an option for continue: "))
    if input_type == 1:
        user = User(users_col)

        print('''
1. User Login
2. User Sign Up''')
        input_type = int(input("Choose an option for continue: "))

        if input_type == 1:
            if user.user_login():
                user.user_operations()
                break
            else:
                print("Try Again.")
        elif input_type == 2:
            user.user_register()       
            
    elif input_type == 2:
        librarian = Librarian(librarian_col)

        if librarian.librarian_login():
            librarian.librarian_operations()
        else:
            print("Try Again.")

    print("\nWelcome to the Library Management System.")    
    print('''
1. User Operations
2. Librarian Operations''')

