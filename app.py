from flask import Flask, jsonify, request

app = Flask(__name__)

users = []
posts = []

@app.route("signup", methods=["POST"])
def signup():
    user = request.get_json()
    if(user.get("username") == None or user.get("avatar") == None ):
        return "Informações inválidas", 400
    users.append(user)
    return "Usuário criado com sucesso", 201

@app.route("/posts", methods=["GET", "POST"])
def get_post_posts():
    if request.method == "GET":
        return jsonify(posts), 200
    elif request.method == "POST":
        post = request.get_json()
        if(post.get("username") == None or post.get("tweet") == None):
            return "Informações inválidas", 400
        if(len(posts) == 10):
            posts.pop()
        posts.insert(0, post)
        return "Post criado", 201

app.run(port=5000, debug=True, host="localhost")