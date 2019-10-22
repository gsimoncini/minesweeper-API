from app import mongo_client, mongo_db
import json
from bson.objectid import ObjectId

class MineSweeperDAO():

    def create_game(self, game):
        games = mongo_db.games
        game_json = json.dumps(game, default=lambda o: getattr(o, '__dict__', str(o)))
        game_dict = json.loads(game_json)
        result = games.insert_one(game_dict)
        game.id = result.inserted_id

    def get_game(self, game_id):
        games = mongo_db.games
        document = games.find_one({'_id': ObjectId(game_id)})
        return document

    def update_game(self, game):
        games = mongo_db.games
        game_json = json.dumps(game, default=lambda o: getattr(o, '__dict__', str(o)))
        game_dict = json.loads(game_json)
        result = games.update_one({'_id': ObjectId(game.id)}, { "$set":game_dict})
        print(result)

mine_sweeper_dao = MineSweeperDAO()
