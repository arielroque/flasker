import os
from flask import Flask, jsonify, request
from routes import Routes

api = Flask(__name__)
routes = Routes(api)

if __name__ == "__main__":
    api.run(host="0.0.0.0", port=os.environ["APP_PORT"], debug=True)
