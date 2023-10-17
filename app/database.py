from os import getenv
from typing import Iterable
from dotenv import load_dotenv
from pymongo import MongoClient


class Database:
    # Loading environment variables
    load_dotenv()
    # Establishing a connection to the MongoDB database
    database = MongoClient(getenv("MONGO_URL"))["Database"]
    # Default projection to exclude the "_id" field
    default_projection = {"_id": False}

    def __init__(self, collection: str):
        """Initialize the database with a specified collection."""
        self.collection = self.database[collection]

    def count(self, query: dict = None) -> int:
        """Count the number of documents based on a query."""
        return self.collection.count_documents(query or {})

    def search(self, search: str, projection: dict = None) -> list[dict]:
        """Search the collection using MongoDB's text search feature."""
        if projection is None:
            projection = self.default_projection
        return list(self.find({"$text": {"$search": search}}, projection=projection))

    def find(self, query: dict = None, projection: dict = None) -> list[dict]:
        """Find documents based on a query and a projection."""
        if projection is None:
            projection = self.default_projection
        return list(self.collection.find(query or {}, projection=projection))

    def find_one(self, query: dict = None, projection: dict = None) -> dict:
        """Find a single document based on a query and a projection."""
        if projection is None:
            projection = self.default_projection
        return self.collection.find_one(query or {}, projection=projection)

    def write_one(self, record: dict):
        """Insert a single document into the collection."""
        self.collection.insert_one(record)

    def write_many(self, records: Iterable[dict]):
        """Insert multiple documents into the collection."""
        self.collection.insert_many(records)

    def update_one(self, query, update):
        """Update a single document based on a query."""
        self.collection.update_one(query, {"$set": update})

    def delete_one(self, query):
        """Delete a single document based on a query."""
        self.collection.delete_one(query)

    def delete_many(self, query):
        """Delete multiple documents based on a query."""
        self.collection.delete_many(query)

    def reset_collection(self):
        """Reset the collection by dropping it and recreating its index."""
        self.database.drop_collection(self.collection.name)
        self.make_index()

    def make_index(self):
        """Create a text index for the collection."""
        self.collection.create_index([("$**", "text")])

    def drop_index(self):
        """Drop all indexes associated with the collection."""
        self.collection.drop_indexes()


if __name__ == '__main__':
    # Test code to reset the collection
    db = Database("collection_name")  # You should specify a collection name here
    db.reset_collection()
