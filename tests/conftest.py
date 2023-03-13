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
    )["mydatabase"]

@pytest.fixture()
def mock_mongo(monkeypatch):
    client = mongomock.MongoClient()
    
    def fake_mongo():
        user = {"username": "Ozgur", "password": "1234", "occupied_books": None}
        book = {'title': '1984', 'id': 16, 'author': 'George Orwell', 'subject_category': 'Novel', 'publication_date': '2012', 'physical_address': 'DD101', 'book_state': 'Reserved'}
        librarian = {"librarian_password": "13579"}

        database = client["mydatabase"]
        books_col = database["books"]
        users_col = database["users"]
        librarian_col = database["librarian"]

        books_col.insert_one(book)
        users_col.insert_one(user)
        librarian_col.insert_one(librarian)
        return database

    monkeypatch.setattr("tests.connection.conn", fake_mongo)
    return fake_mongo()


@pytest.fixture()
def books_col(mock_mongo):    
    books_col = mock_mongo["books"]

    return books_col

@pytest.fixture()
def users_col(mock_mongo):    
    users_col = mock_mongo["users"]

    return users_col

@pytest.fixture()
def librarian_col(mock_mongo):
    librarian_col = mock_mongo["librarian"]

    return librarian_col

@pytest.fixture()
def book_search_object_mock(books_col):
    book_search = BookSearch(books_col)
    return book_search

@pytest.fixture()
def book_object_mock(users_col, books_col):
    book = Book(users_col, books_col)
    return book

@pytest.fixture()
def user_object_mock(users_col, books_col):
    user = User(users_col, books_col)
    return user

@pytest.fixture()
def librarian_object_mock(librarian_col, books_col, users_col):
    librarian = Librarian(librarian_col, books_col, users_col)
    return librarian