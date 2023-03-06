import yaml
import pymongo


with open("db_auth.yaml", encoding="utf8") as file:
    data = yaml.safe_load(file)

db_username = data["username"]
db_password = data["password"]


def conn():
    return pymongo.MongoClient(
        f"mongodb+srv://{db_username}:{db_password}@cluster0.yah8b9u.mongodb.net/?retryWrites=true&w=majority"
    )
