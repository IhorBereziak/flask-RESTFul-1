from flask import Flask
from flask_restful import Api

from config import DevConfig
from app.resources import User

app = Flask(__name__)
app.config.from_object(DevConfig)

api = Api(app)

api.add_resource(User, '/user', '/user/<string:email>')