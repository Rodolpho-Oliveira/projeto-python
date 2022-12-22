from flask import request, Blueprint
from services import create_user

users = []
user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/signup", methods=["POST"])
async def signup():
    user = request.get_json()
    return await create_user(user)