from node import Node
class Tree:
    def __init__(self, contents, turn, max_depth):
        char_map = {"r": True, "y": False}
        initial_board = [[char_map.get(char, None) for char in item] for item in contents.split(",")]
        turn = True if turn == "red" else False

        self.root = Node(initial_board, turn, 0)
        self.max_depth = max_depth

    def traverse(self):
        pass