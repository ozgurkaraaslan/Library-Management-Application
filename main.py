"""Library management application for libraries.

Library users can access library database through this application and 
realize their operations according to the limitations. Library admin can 
reach all database and manage the library system. Authentication is 
required for operations.
"""

import pymongo  # library for mongodb database usage
import yaml  # library for yaml operations

from src.classes.user import User
from src.classes.librarian import Librarian
from src.classes.status import Status

# library imports for user, librarian and status classes

with open("db_auth.yaml") as file:
    data = yaml.safe_load(file)

username = data["username"]
password = data["password"]
# database authentication parameters

client = pymongo.MongoClient(
    f"mongodb+srv://{username}:{password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
)  # database connection establishing

db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]
librarian_col = db["librarian"]
# database collection connections


def user_func():
    """
    Function to monitoring and managing all user operations
    """
    user = User(users_col, books_col)

    print("\n1. User Login\n2. User Sign Up")
    input_type = int(input("Choose an option for continue: "))

    if input_type == 1:
        username = input("\nUsername: ")
        password = input("Password: ")

        response = user.login(username, password)
        if response["status"] == Status.Fail:
            print(response["message"])

        else:
            print("\n" + response["message"])

            while 1:
                print(
                    "\n1. Search books\n2. Reserve a book \n3. Occupy a book\n4. Return a book \n5. Log out"
                )
                try:
                    user_action = int(input("Choose an option for continue: "))
                except:
                    print("Invalid input!")
                    continue

                response = user.operations(user_action)

                print(response["message"])

                if response["status"] == Status.LogOut:
                    break
                if "data" in response.keys():
                    print("\nResult: ")
                    for _data in response["data"]:
                        print(_data)

                input("\nPress enter to continue: ")

    elif input_type == 2:
        username = input("\nUsername: ")
        password = input("Password: ")

        response = user.register(username, password)
        print(response["message"])


def librarian_func():
    """
    Function to monitoring and managing all librarian operations
    """
    librarian = Librarian(librarian_col, books_col, users_col)

    password = input("Password: ")
    response = librarian.login(password)
    if response["status"] == Status.Fail:
        print(response["message"])

    else:
        print(response["message"])

        while 1:
            print(
                "\n1. Show All Books\n2. Show All Users\n3. Add a Book\n4. Remove a Book\n5. Log Out"
            )

            try:
                librarian_action = int(input("Choose an option for continue: "))
            except:
                print("Invalid input!")
                continue

            response = librarian.operations(librarian_action)

            print("\n" + response["message"])

            if response["status"] == Status.LogOut:
                break
            if "data" in response.keys() and (response["status"] != Status.Fail):
                print("\nResult: ")
                for _data in response["data"]:
                    print(_data)

            input("\nPress enter to continue: ")


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
        user_func()

    elif input_type == 2:
        librarian_func()

    elif input_type == 3:
        print("\nApplication is closed. Have a nice day!")
        break
    else:
        print("Invalid input!")

    input("\nPress enter to continue: ")
