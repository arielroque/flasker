class MissingParametersError(Exception):
    def __init__(self, message):
        self.message = message
        self.code = "user-0001"

class UserNotFoundError(Exception):
    def __init__(self, args):
        self.message = "User not found: " + args
        self.code = "user-0002"