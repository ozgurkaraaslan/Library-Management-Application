import pytest
import yaml
import pymongo

from .book import BookSearch
from .status import Status

with open(
    "D:\\SixFab\\Library_Management_Application\\project\\db_auth.yaml",
    encoding="utf8",
) as file:
    data = yaml.safe_load(file)

db_username = data["username"]
db_password = data["password"]
# database authentication parameters

client = pymongo.MongoClient(
    f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
)  # database connection establishing

db = client["mydatabase"]
books_col = db["books"]


def test_search_by_title():

    title = "1984"
    msg = []
    expected_result = books_col.find({"title": title}, {"_id": 0})
    for _data in expected_result:
        msg.append(_data)
    x = BookSearch(books_col)
    res = x.title(title)

    assert res == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    } or res == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": msg,
    }


def test_search_by_author():
    author = "George Orwell"
    msg = []
    expected_result = books_col.find({"author": author}, {"_id": 0})

    for _data in expected_result:
        msg.append(_data)
    x = BookSearch(books_col)
    res = x.author(author)

    assert res == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    } or res == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": msg,
    }


def test_search_by_subject_category():
    subject_category = "Novel"
    msg = []
    expected_result = books_col.find({"subject_category": subject_category}, {"_id": 0})

    for _data in expected_result:
        msg.append(_data)
    x = BookSearch(books_col)
    res = x.subject_category(subject_category)

    assert res == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    } or res == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": msg,
    }


def test_search_by_publication_date():
    publication_date = "2012"
    msg = []
    expected_result = books_col.find({"publication_date": publication_date}, {"_id": 0})

    for _data in expected_result:
        msg.append(_data)
    x = BookSearch(books_col)
    res = x.publication_date(publication_date)

    assert res == {
        "status": Status.Fail,
        "message": "Book does not exist.",
        "data": [],
    } or res == {
        "status": Status.Success,
        "message": "Book exists.",
        "data": msg,
    }
