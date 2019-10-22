import flask
from flask_restful import Api
from pymongo import MongoClient
import config


app = flask.Flask(__name__)
api = Api(app)

mongo_client = MongoClient()
mongo_client = MongoClient(config.MONGO_HOST, config.MONGO_PORT)
mongo_db = mongo_client[config.MONGO_DATABASE]

