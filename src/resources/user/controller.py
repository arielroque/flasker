from resources.user.service import UserService


class UserController:

    def __init__(self):
        self.service = UserService()

    def create_user(self, fields):
        res = self.service.create_user(fields)
        return res
