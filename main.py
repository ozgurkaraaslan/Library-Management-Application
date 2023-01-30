import json
import pymongo
from user_class import User
from librarian_class import Librarian

username = "rebelkrone"
password = "JqlXmO7xuMhkDAoM"

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority")
db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]
librarian_col = db["librarian"]

while 1:
    print("\nWelcome to the Library Management System.")
    print("\n1. User Operations\n2. Librarian Operations\n3. Close Application")
    
    try:
        input_type = int(input("Choose an option for continue: "))
    except:
        print("Invalid input!")
        continue
    
    if input_type == 1:
        user = User(users_col, books_col)

        print("\n1. User Login\n2. User Sign Up")
        input_type = int(input("Choose an option for continue: "))

        if input_type == 1:
            if user.user_login():
                user.user_operations()
                continue
            else:
                print("Try Again.")
        elif input_type == 2:
            user.user_register()       
            
    elif input_type == 2:
        librarian = Librarian(librarian_col, books_col, users_col)

        if librarian.librarian_login():
            librarian.librarian_operations()
        else:
            print("Try Again.")
    elif input_type == 3:
        print("\nApplication is closed. Have a nice day!")
        break
    else:
        print("Invalid input!")

