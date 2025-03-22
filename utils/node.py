class Node:
    def __init__(self, evaluation: int | None):
        self.alpha = - float("inf")
        self.beta = float("inf")
        self.evaluation = evaluation
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

    # def get_turn(self):
    #     return self.turn

    def get_evaluation(self):
        return self.evaluation

    def get_children(self):
        return self.children