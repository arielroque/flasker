from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse

# creating the flask app
app = Flask(__name__)
# creating the api object
api = Api(app)

parser = reqparse.RequestParser()


class Hello(Resource):
    def get(self, id=None):
        return jsonify({'message': 'Hello World Flask'})

    def post(self, id=None):
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        return jsonify({'message': "oi "+str(args['name'])})

    def put(self, id):
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        return jsonify({'message': "atualizando para o nome " + str(args['name'])})

    def delete(self, id):
        parser.add_argument('name', type=str)
        args = parser.parse_args()
        return jsonify({'message': "atualizando para o nome " + str(args['name'])})


api.add_resource(Hello, '/', '/update/<int:id>')

if(__name__ == '__main__'):
    app.run(host='0.0.0.0', port= 5000, debug=True)
