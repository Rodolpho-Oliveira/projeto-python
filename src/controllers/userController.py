from ..services.userService import create_user
import json, falcon

users = []

class UserController:
    async def on_post(self, req, resp):
        user = await req.media
        status = await create_user(user)
        resp.status = status
        if(status == 201):
            resp.text = json.dumps("Usuário criado")
        else:
            resp.text = json.dumps("Informações inválidas")