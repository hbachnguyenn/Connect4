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

    def perform_next_move(self, location: tuple[int, int], turn: bool) -> None:
        self.board[location[0]][location[1]] = turn

    def undo_move(self, location: tuple[int, int]) -> None:
        self.board[location[0]][location[1]] = None

    def display_board(self) -> None:
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                print(self.board[5-row][col], end="\t")
            print()

    def get_board(self):
        return self.board