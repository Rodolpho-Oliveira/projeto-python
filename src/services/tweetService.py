from .userService import users

posts = []
class TweetService:
    async def check_avatar():
        for post in posts:
            for user in users:
                if(post["username"] == user["username"]):
                    post["avatar"] = user["avatar"]
        print(posts)
        return posts

    async def create_post(post):
        if(post.get("username") == None or post.get("tweet") == None):
            return "Informações inválidas", 400
        if(len(posts) == 10):
            posts.pop()
        posts.insert(0, post)