import yaml
import pymongo
import pytest

from src.classes.book import Book, BookSearch
from src.classes.book import Status

with open("db_auth.yaml", encoding="utf8") as file:
    data = yaml.safe_load(file)

db_username = data["username"]
db_password = data["password"]

client = pymongo.MongoClient(
    f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
)
db = client["mydatabase"]
books_col = db["books"]
users_col = db["users"]

book = Book(users_col, books_col)
book_search = BookSearch(books_col)


def test_search_by_title_is_success(search_by_title, _mock_mongo):

    _title = "1984"
    _db = _mock_mongo["mydatabase"]
    books_col_ = _db["books"]
    response = BookSearch(books_col_).title(_title)

    assert response == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": search_by_title,
    }


def test_search_by_title_is_fail():
    _title = "1983"

    response = book_search.title(_title)

    assert response == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_author_is_success(search_by_author):
    _author = "George Orwell"
    response = book_search.author(_author)

    assert response == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": search_by_author,
    }


def test_search_by_author_is_fail():
    _author = "Yasar Kemal"
    response = book_search.author(_author)

    assert response == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_subject_category_is_success(search_by_subject_category):
    _subject_category = "Novel"
    response = book_search.subject_category(_subject_category)
    assert response == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": search_by_subject_category,
    }


def test_search_by_subject_category_is_fail():
    _subject_category = "Religion"
    response = book_search.subject_category(_subject_category)

    assert response == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    }


def test_search_by_publication_date_is_success(search_by_publication_date):
    _publication_date = "2012"
    response = book_search.publication_date(_publication_date)

    assert response == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": search_by_publication_date,
    }


def test_search_by_publication_date_is_fail():
    _publication_date = "2024"
    response = book_search.publication_date(_publication_date)

    assert response == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    }


def test_show(show):
    response = book.show()

    assert response == {
        "status": Status.Success,
        "message": "The books are listed.",
        "data": show,
    }
