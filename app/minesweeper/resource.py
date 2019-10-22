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

api.add_resource(GameResource,'/game',endpoint='Game::CREATE')


class MinesWeeperRevealResource(BaseResource):
    def __init__(self):
        self.bo = MinesWeeperBO()

    def _is_valid_request_body(self, row, col):
        try:
            int(row)
            int(col)
            return True
        except Exception as e:
            pass
        return False

    def post(self, game_id):
        body = request.get_json()
        if 'row' not in body or not body.get('row'):
            raise ValidationError(
                errors=dict(message="Row parameter NOT exists"))
        if 'col' not in body or not body.get('col'):
            raise ValidationError(
                errors=dict(message="Col parameter NOT exists"))
        col = body.get('col')
        row = body.get('row')
        if not self._is_valid_request_body(row, col):
            raise ValidationError(
                errors=dict(message="Row and Col should be numbers."))
        row = int(row)
        col = int(col)
        game = self.bo.reveal_cell(game_id, row, col)
        game_dict = game_schema.dump(game)
        return self._response(game_dict, 200)

api.add_resource(MinesWeeperRevealResource,'/game/<string:game_id>/reveal',endpoint='Game::REVEAL')