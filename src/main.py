"""Library management application for libraries.

Library users can access library database through this application and 
realize their operations according to the limitations. Library admin can 
reach all database and can manage the library system. An authentication is 
required for all.
"""

import pymongo  # library for mongodb database usage
from classes.user_class import User
from classes.librarian_class import Librarian

# libraries for user and librarian classes

username = "rebelkrone"
password = "JqlXmO7xuMhkDAoM"
# database authentication parameters

client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
)  # database connection establishing

db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]
librarian_col = db["librarian"]
# database collection connections

while 1:
    """
    Loop for user interface
    """
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
            if user.login():
                user.operations()
                continue
            else:
                print("Try Again.")
        elif input_type == 2:
            user.register()
    elif input_type == 2:
        librarian = Librarian(librarian_col, books_col, users_col)

        if librarian.login():
            librarian.operations()
        else:
            print("Try Again.")
    elif input_type == 3:
        print("\nApplication is closed. Have a nice day!")
        break
    else:
        print("Invalid input!")
