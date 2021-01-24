from resources.user.api import user_blueprint
from flask import Flask

class Routes:

    def __init__(self,flask):
        self.flask = flask
        self.initialize_routes()

    def __register_routes(self,route):
         self.flask.register_blueprint(route)


    def initialize_routes(self):

        """
        Add all the blueprints of API in the ROUTES variable
        """

        ROUTES = {
            user_blueprint
        }

        for route in ROUTES:
            self.__register_routes(route)
        