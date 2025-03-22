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
        self.root = Node(None)  # Root node

    def generate_state_space_tree(self):
        """ Always starts tree generation from the root node. """
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
                idx = 1 if self.turn else 0
                evalu = score.evaluate_initial_board(board)[idx]

            # add child
            child = Node(evalu)
            node.add_child(child)

            # self.board.display_board()

            # backtrack
            self.turn = False if self.turn else True
            self.expand_tree(child, depth + 1)

            self.turn = False if self.turn else True
            self.board.undo_move(move)


    def traverse(self, node=None):
        pass

    def display_tree(self, node, prefix="-"):
        print(prefix + str(node.evaluation))
        for child in node.children:
            self.display_tree(child, prefix + prefix)

