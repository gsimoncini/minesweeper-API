from marshmallow import  Schema, fields

class CellSchema(Schema):
    col = fields.Int()
    row = fields.Int()
    revealed = fields.Bool()
    isMine = fields.Bool(attribute="is_mine")
    flagged = fields.Bool(attribute="flagged")
    neighborsMines = fields.Int(attribute="neighbors_mines")


class BoardSchema(Schema):
    cols = fields.Int()
    rows = fields.Int()
    numberOfMines = fields.Int(attribute="number_of_mines")
    cells = fields.List(fields.Nested(CellSchema, many=True))


class GameSchema(Schema):
    createdAt = fields.DateTime(attribute="created_at")
    status = fields.Str(attribute="game_state")
    message = fields.Str( attribute="message")
    gameId = fields.Str(allow_none=True,  attribute="id")
    level = fields.Str(attribute="level_name")
    board = fields.Nested(BoardSchema)

game_schema = GameSchema()
