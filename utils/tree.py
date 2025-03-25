from utils.node import Node
from utils.board import Board
import utils.score as score

class Tree:
    char_map = {"red": True, "yellow": False}
    board: [[bool | None]]

    def __init__(self, contents, turn, max_depth):
        self.turn = True if turn == 'red' else False
        self.board = Board(contents)
        self.max_depth = max_depth
        self.nodes_examined = 0
        self.root = self.initialize_root()


    def initialize_root(self):
        result = score.evaluate_initial_board(self.board.board)
        evaluation = 0
        if result[0]: evaluation = 10000 if self.turn else -10000
        if not result[0]: evaluation = score.calculate_evaluation(result[1])
        return Node(evaluation, self.turn, -1)

    def minimax(self, node, depth, max_depth, turn) -> Node:
        if node.is_terminated():
            return node

        if depth == max_depth:
            return node

        evaluation_value = [self.minimax(child, depth + 1, max_depth, turn) for child in node.children]

        if not evaluation_value:
            return node

        self.nodes_examined += len(evaluation_value)
        if turn:
            return max(evaluation_value)
        else:
            return min(evaluation_value)


    def generate_state_space(self):
        self.expand_tree(self.root, 0)

    def expand_tree(self, node, depth):
        if depth == self.max_depth:
            return

        if node.is_terminated():
            return

        # get board for evaluation
        board = self.board.get_board()
        moves = self.board.get_next_moves()
        for move in moves:
            child = self.board.perform_next_move(move, node)
            self.expand_tree(child, depth + 1)
            self.board.undo_move(move)

    def display_tree(self, node, prefix="-"):
        print(prefix + f"({node.evaluation})" + f" ({node.col})")
        for child in node.children:
            self.display_tree(child, prefix + prefix)

