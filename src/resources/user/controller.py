from resources.user.service import UserService
from resources.user.exceptions import MissingParametersError

class UserController:

    def __init__(self):
        self.service = UserService()

    def create_user(self, fields):
        res = {}
        status = 200

        try:
            res = self.service.create_user(fields)

        except MissingParametersError as mpe:
            res['error'] = mpe.message
            res['code'] = mpe.code
            status = 400

        return res,status

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
