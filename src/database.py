import os
from datetime import datetime
from bson import ObjectId
from pymongo import MongoClient

class Database:
    def __init__(self):
        self.db = MongoClient(
            "mongodb://"
            + os.environ["MONGODB_USERNAME"]
            + ":"
            + os.environ["MONGODB_PASSWORD"]
            + "@"
            + os.environ["MONGODB_HOSTNAME"]
            + ":27017/"
            + os.environ["MONGODB_DATABASE"]
        )
        self.db = self.db[os.environ["MONGODB_DATABASE"]]

    def insert(self, element, collection_name):

        element["created"] = datetime.now()
        element["updated"] = datetime.now()

        inserted = self.db[collection_name].insert(element)

        return str(inserted)

    def find(
        self,
        criteria,
        collection_name,
        projetion=None,
        sort=None,
        limit=0,
        cursor=False):

        resp = []

        itens = self.db[collection_name].find(filter=criteria, limit=limit, sort=sort)

        for item in itens:
            if "_id" in item:
                item["_id"] = str(item["_id"])
            resp.append(item)

        return resp

    def find_by_id(self, id, collection_name):
        item = self.find({"_id": ObjectId(id)}, collection_name)
        return item

    def update(self, id, fields, collection_name):
        updated = self.db[collection_name].update_one(
            {"_id": ObjectId(id)}, {"$set": fields}
        )

        return bool(updated.matched_count > 0)

    def delete(self, id, collection_name):
        deleted = self.db[collection_name].delete_one({"_id": ObjectId(id)})
        return bool(deleted.deleted_count > 0)
