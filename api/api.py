from flask import Flask, jsonify, request
#from resources.user.api import user_blueprint
from flask_pymongo import PyMongo

import os

api = Flask(__name__)
#api.register_blueprint(user_blueprint)

api.config["MONGO_URI"] = 'mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + \
    '@' + os.environ['MONGODB_HOSTNAME'] + \
    ':27017/' + os.environ['MONGODB_DATABASE']

mongo = PyMongo(api)
db = mongo.db

print(_todos=db.todo.find())

if(__name__ == '__main__'):
    api.run(host='0.0.0.0', port=5050, debug=True)
