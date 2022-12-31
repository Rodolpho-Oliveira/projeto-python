users = []

async def create_user(user):
    if(user.get("username") == None or user.get("avatar") == None ):
        return 400
    users.append(user)
    return 201