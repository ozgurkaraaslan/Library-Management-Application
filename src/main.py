"""Library management application for libraries.

Library users can access library database through this application and 
realize their operations according to the limitations. Library admin can 
reach all database and can manage the library system. An authentication is 
required for all.
"""

import pymongo  # library for mongodb database usage
import json

from classes.user_class import User
from classes.librarian_class import Librarian
# libraries for user and librarian classes

with open("config/db_auth.json") as file:
    data = json.load(file)

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
    user = User(users_col, books_col)

    print("\n1. User Login\n2. User Sign Up")
    input_type = int(input("Choose an option for continue: "))

    if input_type == 1:
        username = input("\nUsername: ")
        password = input("Password: ")

        if user.login(username, password):
            print("Login is succesfull.")

            while 1:
                print(
                    "\n1. Search books\n2. Reserve a book \n3. Occupy a book\n4. Return a book \n5. Log out"
                )
                try:
                    user_action = int(input("Choose an option for continue: "))
                except:
                    print("Invalid input!")
                    continue

                res = user.operations(user_action)
                
                if type(res) == str:
                    print(res)
                elif type(res) == list:
                    for i in res:
                        print(i)
                else:   
                    if res == 99:
                        print("Invalid input!")
                    elif res == 100:
                        print("Successfully logged out.")
                        break
                input("\nPress enter to continue: ")

        else:
            print("Login is not successfull!")
            print("Try Again.")
            
    elif input_type == 2:
        username = input("\nUsername: ")
        password = input("Password: ")

        if user.register(username, password):
            print("Sign Up is successfull.")
        else:
            print("Sign Up is not succesfull.")

def librarian_func():
    librarian = Librarian(librarian_col, books_col, users_col)

    if librarian.login():
        print("Login is successfull.")

        while 1:
            print("\n1. Show All Books\n2. Show All Users\n3. Add a Book\n4. Remove a Book\n5. Log Out")

            try:
                librarian_action = int(input("Choose an option for continue: "))
            except:
                print("Invalid input!")
                continue
            
            res = librarian.operations(librarian_action)

            if type(res) == str:
                print(res)
            elif type(res) == list:
                for i in res:
                    print(i)
            else:   
                if res == 99:
                    print("Invalid input!")
                elif res == 100:
                    print("Successfully logged out.")
                    break
            input("\nPress enter to continue: ")
            
    else:
        print("Login is not successfull!")
        print("Try Again.")

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
