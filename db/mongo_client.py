from pymongo import MongoClient

def get_db():
    client = MongoClient(
        "mongodb://root:example@localhost:27017/",
        serverSelectionTimeoutMS=2000
    )
    db = client["testdb"]
    return db
