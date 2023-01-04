from ..services.tweetService import TweetService
import json
import falcon

class TweetController:
    async def on_get(self, req, resp):
        posts = await TweetService.check_avatar()
        resp.text = json.dumps(posts)
        resp.status = falcon.HTTP_200

    async def on_post(self, req, resp):
        post = await req.media
        error = await TweetService.create_post(post)
        if error:
            return error
        resp.text = json.dumps("Post criado")
        resp.status = falcon.HTTP_201