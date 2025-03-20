from utils.node import Node
from utils.board import Board
import utils.score as score

class Tree:
    char_map = {"red": True, "yellow": False}
    board: [[bool | None]]

    def __init__(self, contents, turn, max_depth):
        turn = True if turn == 'red' else False
        self.board = Board(contents)
        self.max_depth = max_depth
        self.root = Node(None, None, turn)  # Root node

    def generate_state_space_tree(self):
        """ Always starts tree generation from the root node. """
        self._expand_tree(self.root, 0)  # Always start from root

    def _expand_tree(self, node, depth):
        pass

    def traverse(self, node=None):
        pass
