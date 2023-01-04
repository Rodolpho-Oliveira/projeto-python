from ..services.userService import create_user
import json, falcon

users = []

class UserController:
    async def on_post(self, req, resp):
        user = await req.media
        await create_user(user)
        resp.text = json.dumps("Usuário criado")
        resp.status = falcon.HTTP_201