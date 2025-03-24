class Node:
    def __init__(self, evaluation: int | None, turn: bool, col: int):
        self.alpha = - float("inf")
        self.beta = float("inf")
        self.evaluation = evaluation
        self.turn = turn
        self.col = col
        self.won = False
        self.children = []

    def set_alpha(self, alpha: int):
        self.alpha = alpha

    def set_beta(self, beta: int):
        self.beta = beta

    def add_child(self, child: "Node"):
        self.children.append(child)

    def get_alpha(self):
        return self.alpha

    def get_beta(self):
        return self.beta

    def get_turn(self):
        return self.turn

    def get_col(self):
        return self.col

    def get_won(self):
        return self.won

    def get_evaluation(self):
        return self.evaluation

    def get_children(self):
        return self.children

    def __gt__(self, other):
        return self.evaluation > other.evaluation

    def __lt__(self, other):
        return self.evaluation < other.evaluation
