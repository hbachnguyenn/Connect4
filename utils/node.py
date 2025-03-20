class Node:
    def __init__(self, parent, evaluation: int | None, turn: bool):
        self.turn = turn
        self.alpha = - float("inf")
        self.beta = float("inf")
        self.evaluation = evaluation
        self.parent = parent
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

    def get_parent(self):
        return self.parent

    def get_evaluation(self):
        return self.evaluation

    def get_children(self):
        return self.children