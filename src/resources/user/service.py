from database import Database
import os


class UserService(object):

    def __init__(self):
        self.db = Database()

    def create_user(self, fields):
        res = self.db.insert(fields, 'users')

        return res
