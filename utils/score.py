import math

def count_consecutive_tokens_in_line(board: [[bool | None]], start: tuple[int, int],
                                     red: int, yellow: int, direction: tuple[int, int],
                                     count_token = False) -> tuple[int, int]:
    row, col = start
    previous = None
    streak = 1

    while 0 <= row < len(board) and 0 <= col < len(board[0]):
        print(row, col, board[row][col])


        cur_token = board[row][col]
        if count_token:
            if cur_token is True:
                red += 1
            if cur_token is False:
                yellow += 1

        if cur_token == previous and streak < 4:
            streak += 1
        else:
            if streak > 1 and previous is not None:
                score = int(math.pow(10, streak - 1))
                (red, yellow) = (red + score, yellow) if previous else (
                    red, yellow + score)
                print(streak)
                print(score)
            streak = 1

        if (direction == (0, 1) and col == len(board[0]) - 1) or (direction == (1, 0) and row == len(board) - 1)\
                or ((direction == (1, 1)) and ((row == len(board) - 1) or (col == len(board[0]) - 1))) \
                or ((direction == (-1, 1)) and ((row == 0) or (col == len(board[0]) - 1))):

            if streak > 1 and previous is not None:
                score = int(math.pow(10, streak - 1))
                print("HERE")
                (red, yellow) = (red + score, yellow) if previous else (
                    red, yellow + score)


        previous = cur_token
        row += direction[0]
        col += direction[1]

    print(red, yellow)
    print()
    return red, yellow


def evaluate_initial_board(board: [[bool | None]]):
    red = 0
    yellow = 0
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]

    # Loop through the first row + evaluate all lines pass through these points + count the number of points
    for col in range(len(board[0])):
        red, yellow = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[2], True)
        if col != 6:
            red, yellow = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[1])
        if col != 0:
            red, yellow = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[3])

    print("Start row")
    for row in range(len(board)):
        red, yellow = count_consecutive_tokens_in_line(board, (row, 0), red, yellow, directions[0])
        if row != 0:
            red, yellow = count_consecutive_tokens_in_line(board, (row, 0), red, yellow, directions[1])

    for row in range(len(board)):
        if row != 0 and row != 5:
            red, yellow = count_consecutive_tokens_in_line(board, (row, 6), red, yellow, directions[3])

    return red, yellow

initial_board =     [[None, None, False, False, True, True, True],
                     [None, None, True, False, True, False, True],
                     [None, None, None, None, False, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None],
                     [None, None, None, None, None, None, None]]

for i in reversed(range(len(initial_board))):
    print(initial_board[i])

red_score, yellow_score = evaluate_initial_board(initial_board)
print("RED: ", red_score)
print("YELLOW: ", yellow_score)
