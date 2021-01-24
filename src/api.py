import os

from flask import Flask, jsonify, request

from resources.user.api import user_blueprint

api = Flask(__name__)
api.register_blueprint(user_blueprint)


if __name__ == "__main__":
    api.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)
