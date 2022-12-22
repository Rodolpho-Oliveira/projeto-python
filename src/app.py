from flask import Flask
import routes

app = Flask(__name__)

app.register_blueprint(routes.tweet_blueprint)
app.register_blueprint(routes.user_blueprint)

app.run(port=5000, debug=True, host="localhost")