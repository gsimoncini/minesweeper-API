import flask
from flask_restful import Api
from pymongo import MongoClient
import config


app = flask.Flask(__name__)
api = Api(app)

mongo_client = MongoClient()
mongo_client = MongoClient(config.MONGO_URI, connect=False)
mongo_db = mongo_client[config.MONGO_DATABASE]

@app.route('/')
def hello_world():
    return 'Hello, World!'

from app.minesweeper.resource import *



if __name__ == '__main__':
    app.run()

