from flask import request, jsonify, Blueprint
from .userController import users

posts = []

tweet_blueprint = Blueprint("tweet_blueprint", __name__)

@tweet_blueprint.route("/posts", methods=["GET", "POST"])
def get_post_posts():
    if request.method == "GET":
        for post in posts:
            for user in users:
                if(post["username"] == user["username"]):
                    post["avatar"] = user["avatar"]
        return jsonify(posts), 200
    elif request.method == "POST":
        post = request.get_json()
        if(post.get("username") == None or post.get("tweet") == None):
            return "Informações inválidas", 400
        if(len(posts) == 10):
            posts.pop()
        posts.insert(0, post)
        return "Post criado", 201