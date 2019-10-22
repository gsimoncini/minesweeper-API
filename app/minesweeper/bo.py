from app.minesweeper.model import Game, LEVELS
from app.base.exceptions import ValidationError
from app.minesweeper.dao import mine_sweeper_dao

class MinesWeeperBO():
    def create_mines_weeper(self, level):
        if level.lower()  not in LEVELS:
            raise ValidationError("Level {}  is not valid. Must be Easy, Medium or Hard")
        game = Game(level.lower())
        mine_sweeper_dao.create_game(game)
        return game
