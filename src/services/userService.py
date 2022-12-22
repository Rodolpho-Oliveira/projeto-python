users = []

async def create_user(user):
    if(user.get("username") == None or user.get("avatar") == None ):
        return 400
        exit()
    users.append(user)