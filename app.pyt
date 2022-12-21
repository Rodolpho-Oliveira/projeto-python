from flask import Flask, jsonify, request

app = Flask(__name__)

posts = []

@app.route("/posts", methods=["GET", "POST"])
def get_post_posts():
    if request.method == "GET":
        return jsonify(posts), 200
    elif request.method == "POST":
        post = request.get_json()
        if(len(posts) == 10):
            posts.pop()
        posts.insert(0, post)
        return "Post criado", 201

app.run(port=5000, debug=True, host="localhost")