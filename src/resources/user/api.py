from flask import Blueprint, request, jsonify
from resources.user.controller import UserController
user_blueprint = Blueprint('users', __name__, url_prefix="/users")


@user_blueprint.route("", methods=["POST"])
def create_user():

    fields = request.get_json(force=True)
    res = UserController().create_user(fields)
    return res
