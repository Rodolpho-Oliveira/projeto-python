from flask import Blueprint
from controllers import signup

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/signup", methods=["POST"])
def register():
    return signup()
