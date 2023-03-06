import yaml
import pymongo

from src.classes.librarian import Librarian
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
librarian_col = db["librarian"]

librarian = Librarian(librarian_col, books_col, users_col)


def test_login_is_success():
    _librarian_password = "13579"

    response = librarian.login(_librarian_password)

    assert response == {"status": Status.Success, "message": "Login is successful."}


def test_login_is_fail():
    _librarian_password = "02468"

    response = librarian.login(_librarian_password)

    assert response == {"status": Status.Fail, "message": "Login is not successful."}
