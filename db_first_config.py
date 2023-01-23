import pymongo

username = "rebelkrone"
password = "JqlXmO7xuMhkDAoM"

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
                "stock_quantity": 2,
                "book_state": "Free"
            },
            {
                "title": "Improbable",
                "id": 2,
                "author": "Adam Fawer",
                "subject_category": "Science-Fiction",
                "publication_date": "2012",
                "physical_address": "AA112",
                "stock_quantity": 4,
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
