from flask import Blueprint
from controllers import get_post_posts

tweet_blueprint = Blueprint("tweet_route_blueprint", __name__)

@tweet_blueprint.route("/posts", methods=["GET", "POST"])
async def create_show_posts():
    return await get_post_posts()