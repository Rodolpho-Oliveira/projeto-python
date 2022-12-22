from flask import request, Blueprint

users = []
user_blueprint = Blueprint("user_blueprint", __name__)

@user_blueprint.route("/signup", methods=["POST"])
def signup():
    user = request.get_json()
    if(user.get("username") == None or user.get("avatar") == None ):
        return "Informações inválidas", 400
    users.append(user)
    return "Usuário criado com sucesso", 201