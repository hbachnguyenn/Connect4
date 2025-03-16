from state import State

class Node:
    def __init__(self, board: [[bool | None]], turn: bool, depth: int):
        self.turn = True if turn == 'red' else False
        self.alpha = - float("inf")
        self.beta = float("inf")
        self.depth = depth
        self.state = State(board)

    def generate_children(self):
        pass

    def set_alpha(self, alpha: int):
        self.alpha = alpha

    def set_beta(self, beta: int):
        self.beta = beta

    def get_alpha(self):
        return self.alpha

    def get_beta(self):
        return self.beta