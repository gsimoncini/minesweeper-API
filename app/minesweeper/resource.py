from flask import request, json
from flask_restful import Resource
from app import app, api
from app.minesweeper.bo import MinesWeeperBO
from app.minesweeper.schema import game_schema
from app.base.exceptions import ValidationError


class BaseResource(Resource):
    def _response(self, response, status, mimetype='application/json', headers=None):
        response = app.response_class(
            json.dumps(response),
            mimetype=mimetype,
            status=status
        )
        if headers:
            for k, v in headers.iteritems():
                response.headers[k] = v
        return response

class GameResource(BaseResource):
    def __init__(self):
        self.bo = MinesWeeperBO()
    def post(self):
        body = request.get_json()
        if 'level' not in body or not body.get('level'):
            raise ValidationError(
                errors=dict(message="Level is not Valid"))
        game = self.bo.create_mines_weeper(body.get('level'))
        game_dict = game_schema.dump(game)
        return self._response(game_dict, 201)

api.add_resource(GameResource,'/game',endpoint='MinesWeeper::CREATE')

