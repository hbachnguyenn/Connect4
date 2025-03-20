## Board function
initial_board =     [[None, None, False, False, True, True, True],
                     [None, None, True, False, True, False, True],
                     [None, None, None, None, False, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]

def get_next_moves(board: [[bool | None]]) -> [tuple[int, int]]:
    next_moves = []
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] is None:
                next_moves.append((row, col))
                break
    return next_moves

def perform_next_move(board: [[bool | None]], location: tuple[int, int], turn: bool) -> None:
    board[location[0]][location[1]] = turn

def undo_move(board: [[bool | None]], location: tuple[int, int]) -> None:
    board[location[0]][location[1]] = None

def generate_next_board(board: [[bool | None]]):
    next_moves = get_next_moves(board)
    for location in next_moves:
        print(location)
        perform_next_move(board, location, turn=True)
        display_board(board)
        undo_move(board, location)

def display_board(board: [[bool | None]]) -> None:
    for row in range(len(board)):
        for col in range(len(board[0])):
            print(board[5-row][col], end="\t")
        print()

if __name__ == '__main__':
    generate_next_board(initial_board)