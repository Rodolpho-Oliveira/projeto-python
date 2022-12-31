from ..services.userService import create_user

users = []

class UserController:
    async def on_post(self, req, resp):
        user = await req.media
        return await create_user(user)