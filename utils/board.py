import utils.score as score
from utils.node import Node

class Board:
    char_map = {"r": True, "y": False}
    board: [[bool | None]]

    def __init__(self, contents: str):
        self.board = [[self.char_map.get(char, None) for char in item] for item in contents.split(",")]

    def get_next_moves(self) -> [tuple[int, int]]:
        next_moves = []
        for col in range(len(self.board[0])):
            for row in range(len(self.board)):
                if self.board[row][col] is None:
                    next_moves.append((row, col))
                    break
        return next_moves

    def perform_next_move(self, position: tuple[int, int], parent: Node) -> Node:
        result = score.update_evaluation_when_add_move(position, self.board, parent.turn)
        if result[0]:
            evaluation = 10000 if parent.turn else -10000
        else:
            evaluation = parent.get_evaluation() + score.calculate_evaluation(result[1])
        node = Node(evaluation, not parent.turn, position[1])
        parent.add_child(node)
        return node

    def undo_move(self, location: tuple[int, int]) -> None:
        self.board[location[0]][location[1]] = None

    def display_board(self) -> None:
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                print(self.board[5-row][col], end="\t")
            print()
        print()
        print("---------------------------------------------------------")
        print()


    def get_board(self):
        return self.board