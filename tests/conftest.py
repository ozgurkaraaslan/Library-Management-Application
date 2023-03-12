import pytest
import yaml
import pymongo
import mongomock

from src.classes.book import Book, BookSearch
from src.classes.user import User
from src.classes.librarian import Librarian

def conn():
    with open("db_auth.yaml", encoding="utf8") as file:
        data = yaml.safe_load(file)

    db_username = data["username"]
    db_password = data["password"]

    return pymongo.MongoClient(
        f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
    )

@pytest.fixture()
def mock_mongo(monkeypatch):
    client = mongomock.MongoClient()

    def fake_mongo():
        user = {"username": "Ozgur", "password": "1234", "occupied_books": None}
        book = {'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}
        librarian = {"librarian_password": "13579"}

        db = client["mydatabase"]
        books_col = db["books"]
        users_col = db["users"]
        librarian_col = db["librarian"]

        books_col.insert_one(book)
        users_col.insert_one(user)
        librarian_col.insert_one(librarian)

        return client

    monkeypatch.setattr("tests.connection.conn", fake_mongo)
    fake_mongo()
    return client

@pytest.fixture()
def book_search_object_mock(mock_mongo):    
    db = mock_mongo["mydatabase"]
    books_col = db["books"]

    book_search = BookSearch(books_col)
    return book_search

@pytest.fixture()
def book_object_mock(mock_mongo):  
    db = mock_mongo["mydatabase"]
    books_col = db["books"]
    users_col = db["users"]

    book = Book(users_col, books_col)
    return book

@pytest.fixture()
def user_object_mock(mock_mongo):  
    db = mock_mongo["mydatabase"]
    books_col = db["books"]
    users_col = db["users"]

    user = User(users_col, books_col)
    return user

@pytest.fixture()
def librarian_object_mock(mock_mongo):  
    db = mock_mongo["mydatabase"]
    librarian_col = db["librarian"]
    books_col = db["books"]
    users_col = db["users"]

    librarian = Librarian(librarian_col, books_col, users_col)
    return librarian