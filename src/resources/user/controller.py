from resources.user.service import UserService


class UserController:

    def __init__(self):
        self.service = UserService()

    def create_user(self, fields):
        res = self.service.create_user(fields)
        return res

    def get_users(self):
        res = self.service.get_users()
        return res

    def get_user(self,user_id):
        res = self.service.get_user(user_id)
        return res

    def update_user(self,user_id,fields):
        res = self.service.update_user(user_id,fields)
        return res

    def delete_user(self,user_id):
        res = self.service.delete(user_id)
        return res   
