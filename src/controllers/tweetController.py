from flask import request, jsonify
from services import check_avatar, create_post

async def get_post_posts():
    if request.method == "GET":
        posts = await check_avatar()
        return jsonify(posts), 200
    elif request.method == "POST":
        post = request.get_json()
        error = await create_post(post)
        if error:
            return error
        return "Post criado", 201