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
    """ Class that represents the game object. """
    def __init__(self, level, created_at = None, id = None, game_state = None, board = None, message = None, finished_at = None, duration = None ):
        self.created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f') if created_at else  datetime.now()
        self.level_name = level
        self.rows, self.cols, self.number_of_mines = LEVELS[level]
        self.id = id
        self.game_state = game_state if game_state else  GAME_STATE_STARTED
        self.board = board if board else Board(self.rows, self.cols, self.number_of_mines)
        self.Message = message
        self.finished_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S.%f') if finished_at else None
        self.duration = duration if duration else None

    @classmethod
    def from_dict(cls, game_dict):
    	return cls(level=game_dict.get('level_name'), created_at=game_dict.get('created_at'), id=game_dict.get('id'), game_state=game_dict.get('game_state'),
                   board=Board.from_dict(game_dict.get('board')), message=game_dict.get('message'), finished_at = game_dict.get('finished_at'),
                   duration = game_dict.get('duratio '))

    def is_finished(self):
        """ Calculates if the game is finished. The game is finished if all the cells that are not mines are revealed """
        cells_status = [list(map(lambda cell: cell.is_mine or (not cell.is_mine and cell.revealed), l)) for l in self.board.cells]
        return all([reduce((lambda x, y: x and y), l) for l in cells_status])

class Board():
    """ Class that represents the board object. """
    def __init__(self, rows, cols, number_of_mines, cells = None):
        self.rows = rows
        self.cols = cols
        self.number_of_mines = number_of_mines
        self.cells = cells if cells else self._create_cells()

    @classmethod
    def from_dict(cls, board_dict):
        cells_matrix = board_dict.get('cells')
        nested_list = [[Cell.from_dict(cell_dict) for cell_dict in rows] for rows in cells_matrix]
        return cls(rows=board_dict.get('rows'), cols=board_dict.get('cols'), number_of_mines=board_dict.get('number_of_mines'),cells=nested_list)

    def _create_cells(self):
        """ Method that creates the cells of the board based on the amount of rows, cols and mines. It uses the shuffle method of the random library.
            It calculates the value of the neighbors_mines for every cell in the board.
         """
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
    """ Class that represents the cell object. """
    def __init__(self, row, col, is_mine, revealed = False, flagged = False, neighbors_mines = 0):
        self.row = row
        self.col = col
        self.is_mine = is_mine
        self.revealed = revealed
        self.flagged = flagged
        self.neighbors_mines = neighbors_mines

    def get_neighbours(self, cells, rows, cols):
        """ Method that returns a generator for every neighbor of the cell in order to iterate over the direct neighbors of the cell."""
        neighbours = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
        for (dx, dy) in neighbours:
            row_offset = self.row + dx
            col_offset = self.col + dy
            if (row_offset > -1 and row_offset < rows) and (col_offset > -1 and col_offset < cols):
                yield cells[row_offset][col_offset]

    def reveal(self, cells, rows, cols):
        """ Method that reveal cell recursively just if the cell has not mines neighbors."""
        self.revealed = True
        if self.neighbors_mines == 0:
            for neighbour in self.get_neighbours(cells, rows, cols):
                if not neighbour.revealed:
                    neighbour.reveal(cells, rows, cols)

    @classmethod
    def from_dict(cls, cell_dict):
    	return cls(row=cell_dict.get('row'), col=cell_dict.get('col'), is_mine=cell_dict.get('is_mine'), revealed=cell_dict.get('revealed'),
                   flagged=cell_dict.get('flagged'), neighbors_mines=cell_dict.get('neighbors_mines'))