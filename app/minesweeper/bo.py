from app.minesweeper.model import Game, LEVELS
from app.base.exceptions import ValidationError
from app.minesweeper.dao import mine_sweeper_dao
from app.minesweeper.model import GAME_STATE_STARTED, GAME_STATE_PLAYING, GAME_STATE_LOSE, GAME_STATE_WIN

class MinesWeeperBO():
    def create_mines_weeper(self, level):
        if level.lower()  not in LEVELS:
            raise ValidationError("Level {}  is not valid. Must be Easy, Medium or Hard")
        game = Game(level.lower())
        mine_sweeper_dao.create_game(game)
        return game

    def _is_valid_request_body(self, row, col, game):
        return row >= 0 and row <=(game.rows -1) and col >= 0 and col <=(game.cols -1)

    def reveal_cell(self, game_id, row, col):
        game_document = mine_sweeper_dao.get_game(game_id)
        if not game_document:
            raise ValidationError("The game {} is NOT Valid.".format(game_id))
        game_document["id"] = game_document["_id"]
        del game_document["_id"]
        game = Game.from_dict(game_document)
        if not self._is_valid_request_body(row, col, game):
            raise ValidationError("The cell point (row,col)->({},{}) is NOT Valid for the game {}.".format(row, col, game_id))
        if game.game_state == GAME_STATE_LOSE or game.game_state == GAME_STATE_WIN:
            raise ValidationError("The game {} is finished. Start one again.".format(game_id))
        if game.game_state == GAME_STATE_STARTED:
            game.game_state = GAME_STATE_PLAYING
        cell = game.board.cells[row][col]
        if cell.revealed:
            game.message = "The cell ({},{}) is already revelead.".format(row, col)
        elif cell.is_mine:
            game.message = "The cell ({},{}) is a mine. GAME OVER.".format(row, col)
            game.game_state = GAME_STATE_LOSE
        else:
            cell.reveal(game.board.cells, game.board.rows, game.board.cols)
            game.message = "Reveal of the cell ({},{}).".format(row, col)
            if game.is_finished():
                game.game_state = GAME_STATE_WIN
                game.message = game.message + " YOU HAVE WON."
        mine_sweeper_dao.update_game(game)
        return game

