from app.minesweeper.model import Game, LEVELS
from app.base.exceptions import ValidationError

class MinesWeeperBO():
    def create_mines_weeper(self, level):
        if level.lower()  not in LEVELS:
            raise ValidationError("Level {}  is not valid. Must be Easy, Medium or Hard")
        game = Game(level.lower())
        return game
