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
        self.nodes_examined = 1
        self.root = self.initialize_root()
        self.board.display_board()
        print(score.evaluate_initial_board(self.board.board))

    def initialize_root(self):
        result = score.evaluate_initial_board(self.board.board)
        evaluation = 0
        if result[0]: evaluation = 10000 if self.turn else -10000
        if not result[0]: evaluation = score.calculate_evaluation(result[1])
        return Node(evaluation, self.turn, 0)

    def minimax(self, node, turn) -> Node | None:
        self.nodes_examined += 1
        if node.is_terminal_node() or node.is_leaf_node():
            node.set_value(node.evaluation)
            return node

        for child in node.get_children():
            if child.get_value() == float("inf") or child.get_value() == float("-inf"):
                self.minimax(child, not turn)

            if node.get_turn() and child.get_value() > node.get_value():
                node.set_value(child.get_value())
                node.set_selected_child(child)
            if not node.get_turn() and child.get_value() < node.get_value():
                node.set_value(child.get_value())
                node.set_selected_child(child)

        if node == self.root:
            return node.get_selected_child()

        return None


    def generate_state_space(self):
        self.expand_tree(self.root, 0)

    def expand_tree(self, node, depth):
        if depth == self.max_depth:
            return

        if node.is_terminal_node():
            return

        # get board for evaluation
        board = self.board.get_board()
        moves = self.board.get_next_moves()
        for move in moves:
            child = self.board.perform_next_move(move, node)
            self.expand_tree(child, depth + 1)
            self.board.undo_move(move)

    def display_tree(self, node, prefix=" " * 8, start_depth = 0):
        print(f"{start_depth} " + prefix + f"({node.get_evaluation()})" + f"\t({node.get_col()})" + f"\t({node.get_turn()})")
        for child in node.children:
            self.display_tree(child, prefix + " " * 8, start_depth + 1)
