import pytest
import yaml
import pymongo
import mongomock

with open("db_auth.yaml", encoding="utf8") as file:
    data = yaml.safe_load(file)

db_username = data["username"]
db_password = data["password"]
# database authentication parameters

client = pymongo.MongoClient(
    f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
)  # database connection establishing

db = client["mydatabase"]
books_col = db["books"]


def conn():
    return pymongo.MongoClient(
        f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
    )


@pytest.fixture()
def _mock_mongo(monkeypatch):
    _client = mongomock.MongoClient()

    def fake_mongo():
        return _client

    monkeypatch.setattr("tests.conftest.conn", fake_mongo)
    return _client


@pytest.fixture
def search_by_title():

    title = "1984"
    msg = []
    expected_result = books_col.find({"title": title}, {"_id": 0})
    print(expected_result)
    for _data in expected_result:
        msg.append(_data)

    return msg


@pytest.fixture
def search_by_author():
    author = "George Orwell"
    msg = []
    expected_result = books_col.find({"author": author}, {"_id": 0})
    for _data in expected_result:
        msg.append(_data)

    return msg


@pytest.fixture
def search_by_subject_category():
    subject_category = "Novel"
    msg = []
    expected_result = books_col.find({"subject_category": subject_category}, {"_id": 0})
    for _data in expected_result:
        msg.append(_data)

    return msg


@pytest.fixture
def search_by_publication_date():
    publication_date = "2012"
    msg = []
    expected_result = books_col.find({"publication_date": publication_date}, {"_id": 0})
    for _data in expected_result:
        msg.append(_data)

    return msg


@pytest.fixture
def show():
    msg = []
    for _data in books_col.find({}, {"_id": 0}):
        msg.append(_data)

    return msg
