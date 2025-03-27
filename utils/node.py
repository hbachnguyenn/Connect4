class Node:
    def __init__(self, evaluation: int, turn: bool, col: int):
        self.value = float("-inf") if turn else float("inf")
        self.selected_child = None

        self.evaluation = evaluation
        self.turn = turn
        self.col = col
        self.children = []

    def set_value(self, value: int) -> None:
        self.value = value

    def set_selected_child(self, child: "Node") -> None:
        self.selected_child = child

    def add_child(self, child: "Node"):
        self.children.append(child)

    def get_value(self) -> float | int:
        return self.value

    def get_turn(self) -> bool:
        return self.turn

    def get_col(self) -> int:
        return self.col

    def get_evaluation(self) -> int:
        return self.evaluation

    def get_children(self) -> ['Node']:
        return self.children

    def get_selected_child(self) -> "Node":
        return self.selected_child

    def is_terminal_node(self) -> bool:
        return self.evaluation == 10000 or self.evaluation == -10000

    def is_leaf_node(self) -> bool:
        return len(self.children) == 0
