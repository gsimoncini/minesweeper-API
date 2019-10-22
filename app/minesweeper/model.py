from random import shuffle
from datetime import datetime
from functools import reduce

LEVELS = {
    "easy" : (8, 8, 10),
    "medium":(16, 16, 40),
    "hard": (24, 24, 99)
}


GAME_STATE_STARTED = "Started"
GAME_STATE_WIN = "Win"
GAME_STATE_LOSE = "Lose"
GAME_STATE_PLAYING = "Playing"

class Game():
    def __init__(self, level, created_at = None, id = None, game_state = None, board = None, message = None):
        self.created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f') if created_at else  datetime.now()
        self.level_name = level
        self.rows, self.cols, self.number_of_mines = LEVELS[level]
        self.id = id
        self.game_state = game_state if game_state else  GAME_STATE_STARTED
        self.board = board if board else Board(self.rows, self.cols, self.number_of_mines)
        self.Message = message

class Board():
    def __init__(self, rows, cols, number_of_mines, cells = None):
        self.rows = rows
        self.cols = cols
        self.number_of_mines = number_of_mines
        self.cells = cells if cells else self._create_cells()

    def _create_cells(self):
        mines_locations = [True] * self.number_of_mines
        mines_locations += [False] * (self.cols * self.rows - self.number_of_mines)
        shuffle(mines_locations)
        cells = [[Cell(row, col, is_mine = mines_locations[col*row])
                        for col in range(self.cols)] for row in range(self.rows)]

        for row in cells:
            for cell in row:
                for neighbour in cell.get_neighbours(cells, self.rows, self.cols):
                    if neighbour.is_mine:
                        cell.neighbors_mines += 1
        return cells

class Cell():
    def __init__(self, row, col, is_mine, revealed = False, flagged = False, neighbors_mines = 0):
        self.row = row
        self.col = col
        self.is_mine = is_mine
        self.revealed = revealed
        self.flagged = flagged
        self.neighbors_mines = neighbors_mines

    def get_neighbours(self, cells, rows, cols):
        neighbours = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        for (dx, dy) in neighbours:
            row_offset = self.row + dx
            col_offset = self.col + dy
            if (row_offset > -1 and row_offset < rows) and (col_offset > -1 and col_offset < cols):
                yield cells[row_offset][col_offset]