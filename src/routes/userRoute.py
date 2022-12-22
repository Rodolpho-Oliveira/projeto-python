from flask import Blueprint
from controllers import signup

user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/signup", methods=["POST"])
async def register():
    error = await signup()
    if error:
        return "Informações inválidas", 400
    return "Usuário criado com sucesso", 201
