from bson import ObjectId
from db.mongo_client import get_db

class MovieDAO:
    def __init__(self):
        self.db = get_db()
        self.collection = self.db["movies"]

    def create_movie(self, data: dict) -> str:
        result = self.collection.insert_one(data)
        return str(result.inserted_id)

    def get_movie(self, movie_id: str) -> dict | None:
        return self.collection.find_one({"_id": ObjectId(movie_id)})

    def list_movies(self) -> list[dict]:
        return list(self.collection.find())

    def update_movie(self, movie_id: str, update: dict) -> bool:
        result = self.collection.update_one(
            {"_id": ObjectId(movie_id)},
            {"$set": update}
        )
        return result.modified_count > 0

    def delete_movie(self, movie_id: str) -> bool:
        result = self.collection.delete_one({"_id": ObjectId(movie_id)})
        return result.deleted_count > 0
