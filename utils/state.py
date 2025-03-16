import score
from board import Board

class State:
    def __init__(self, board: [[bool | None]], row = None, col = None, diagonal = None):
        self.board = Board(board)
        self.evaluation_value = 0

    def get_evaluation_value(self):
        return self.evaluation_value

    def generate_next_state(self):
        pass