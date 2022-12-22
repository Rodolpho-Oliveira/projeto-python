from flask import Flask
import controllers

app = Flask(__name__)

app.register_blueprint(controllers.tweet_blueprint)
app.register_blueprint(controllers.user_blueprint)

app.run(port=5000, debug=True, host="localhost")