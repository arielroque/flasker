from database import Database
from flask import jsonify
import os

class UserService(object):

    def __init__(self):
        self.collection_name = "users"
        self.db = Database()

    def create_user(self, fields):
        res = self.db.insert(fields, self.collection_name)

        return res

    def get_users(self):
        users = self.db.find(None, self.collection_name)

        res = jsonify(
            status=200, users=users)

        return res

    def get_user(self, user_id):
        user = self.db.find_by_id(user_id, self.collection_name)

        res = jsonify(
            status=200, user=user)

        return res

    def update_user(self, user_id, fields):
        res = jsonify(
            status=200, message=f"User {user_id} successfully updated")

        is_updated = self.db.update(user_id, fields, self.collection_name)

        if(not is_updated):
            pass

        return res

    def delete(self, user_id):
        res = jsonify(
            status=200, message=f"User {user_id} successfully deleted")

        is_deleted = self.db.delete(user_id, self.collection_name)

        if(not is_deleted):
            pass

        return res
