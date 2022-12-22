from flask import Blueprint
from controllers import get_post_posts

tweet_blueprint = Blueprint("tweet_route_blueprint", __name__)

@tweet_blueprint.route("/posts", methods=["GET", "POST"])
def create_show_posts():
    return get_post_posts()