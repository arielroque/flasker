from flask import Blueprint, request, jsonify
from resources.user.controller import UserController
user_blueprint = Blueprint('users', __name__, url_prefix="/users")


@user_blueprint.route("", methods=["POST"])
def create_user():

    fields = request.get_json(force=True)
    res = UserController().create_user(fields)
    return res


@user_blueprint.route("", methods=["GET"])
def get_users():
    res = UserController().get_users()
    return res


@user_blueprint.route("/<user_id>", methods=["GET"])
def get_user(user_id):

    res = UserController().get_user(user_id)
    return res


@user_blueprint.route("/<user_id>", methods=["DELETE"])
def delete_user(user_id):

    res = UserController().delete_user(user_id)
    return res
