import falcon.asgi
from .controllers.tweetController import *
from .controllers.userController import *

app = falcon.asgi.App()

app.add_route('/tweet', TweetController())
app.add_route('/signup', UserController())