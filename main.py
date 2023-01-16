import json

db = [{
        "book": [
            {
                "title": "",
                "id": None,
                "author": "",
                "subject_category": "",
                "publication_date": "",
                "physical_address": "",
                "stock_quantity": None,
                "book_state": ""
            }
        ]
    },
    {
        "user": [
            {
                "username": "Ozgur",
                "password": 456,
                "occupied_books": [""]
            }
        ]
    },
    {
        "librarian_password": 1234
    }]

print("Welcome to the Library Management System.")
print('''
1. Librarian Login
2. User Login
3. User Sign Up''')

def librarian_login(passwd):
    if passwd == db[2]["librarian_password"]:
        print("Login is successfull.")
    else:
        print("Login is not successfull!")

def user_login(uname, passwd):
    for i in db[1]["user"]:
        if i["username"] == uname:
            if i["password"] == passwd:
                print("Login Succesfull.")
            else:
                print("Login is not successfull!")
            return 

    print("User not found!")   

while 1:
    input_type = int(input("Choose an option for continue: "))
    if input_type == 1:
        librarian_password = int(input("Password: "))
        librarian_login(librarian_password)
        break
    elif input_type == 2:
        username = input("Username: ")
        password = int(input("Password: "))
        user_login(username, password)
        break
    elif input_type == 3:
        username = input("New Username: ")
        password = input("New Password: ")
        user_register(username, password)
        break
    else:
        print("Invalid input! Try again.\n")

