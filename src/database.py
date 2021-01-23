from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
import os

class Database:

    def __init__(self):
        self.db = MongoClient('mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] +
                              '@' + os.environ['MONGODB_HOSTNAME'] +
                              ':27017/'+os.environ['MONGODB_DATABASE'])
        self.db = self.db[os.environ['MONGODB_DATABASE']]

    def insert(self, element, collection_name):
        element["created"] = datetime.now()
        element["updated"] = datetime.now()

        inserted = self.db[collection_name].insert(element)

        return str(inserted)

    def find(self, criteria, collection_name, projetion=None, sort=None, limit=0, cursor=False):
        pass

    def find_by_id(self, id, collection_name):
        pass

    def update(self, element, collection_name):
        pass

    def delete(self, id, collection_name):
        pass
