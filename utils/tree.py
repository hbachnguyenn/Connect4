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
        self.root = Node(None, self.turn, -1)  # Root node
        self.nodes_examined = 0

    def minimax(self, node, depth, max_depth, turn) -> Node:
        if node.won:
            node.evaluation = 10000 if node.turn else -10000
            return node

        if depth == max_depth:
            return node
        # red
        evaluation_value = [self.minimax(child, depth + 1, max_depth, turn) for child in node.children]
        if not evaluation_value:
            return node
        self.nodes_examined += len(evaluation_value)
        if turn:
            return max(evaluation_value)
        else:
            return min(evaluation_value)


    def generate_state_space_tree(self):
        self.expand_tree(self.root, 0)  # Always start from root

    def expand_tree(self, node, depth):
        if depth == self.max_depth:
            return
        # get board for evaluation
        board = self.board.get_board()
        moves = self.board.get_next_moves()
        for move in moves:
            self.board.perform_next_move(move, self.turn)

            evalu = None
            if depth == self.max_depth - 1:
                red = score.evaluate_initial_board(board, True)
                yellow = score.evaluate_initial_board(board, False)
                evalu = -1 if red == -1 or yellow == -1 else red - yellow

            # add child
            child = Node(evalu, False if self.turn else True, move[1])
            if evalu == -1:  # win
                child.won = True
                node.add_child(child)
                return
            node.add_child(child)

            self.turn = False if self.turn else True
            self.expand_tree(child, depth + 1)
            # backtrack
            self.turn = False if self.turn else True
            self.board.undo_move(move)

    def display_tree(self, node, prefix="-"):
        print(prefix + f"({node.evaluation})")
        for child in node.children:
            self.display_tree(child, prefix + prefix)

