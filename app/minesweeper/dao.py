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

mine_sweeper_dao = MineSweeperDAO()
