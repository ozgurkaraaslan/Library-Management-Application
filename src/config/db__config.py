import pymongo
import json

with open("config/db_auth.json") as file:
    data = json.load(file)

username = data["username"]
password = data["password"]

client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority")

db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]
librarian_col = db["librarian"]

books = [
            {
                "title": "What Men Live By",
                "id": 1,
                "author": "Lev Nikolayeviç Tolstoy",
                "subject_category": "Novel",
                "publication_date": "2010",
                "physical_address": "AA111",
                "book_state": "Free"
            },
            {
                "title": "Improbable",
                "id": 2,
                "author": "Adam Fawer",
                "subject_category": "Science-Fiction",
                "publication_date": "2012",
                "physical_address": "AA211",
                "book_state": "Free"
            },
            {
                "title": "Clean Code:A Handbook of Agile Software Craftsmanship",
                "id": 3,
                "author": "Robert C. Martin",
                "subject_category": "Engineering",
                "publication_date": "2008",
                "physical_address": "AA311",
                "book_state": "Free"
            }

        ]
users = [
            {
                "username": "Ozgur",
                "password": 1234,
                "occupied_books": None
            },
            {
                "username": "Ahmet",
                "password": 5678,
                "occupied_books": None
            }
        ]
librarian = {"librarian_password": 13579}

books_col.insert_many(books)
users_col.insert_many(users)
librarian_col.insert_one(librarian)
