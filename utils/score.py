import math

# def count_consecutive_tokens_in_line(board: [[bool | None]], start: tuple[int, int],
#                                      red: int, yellow: int, direction: tuple[int, int],
#                                      count_token = False) -> tuple[int, int, bool | None]:
#     row, col = start
#     previous = None
#     streak = 1
#     is_win = False
#
#     while 0 <= row < len(board) and 0 <= col < len(board[0]):
#         is_win = None
#         cur_token = board[row][col]
#         if count_token:
#             if cur_token is True:
#                 red += 1
#             if cur_token is False:
#                 yellow += 1
#
#         if cur_token == previous and streak < 4:
#             streak += 1
#             if streak == 4:
#                 is_win = True
#                 break
#
#         else:
#             if streak > 1 and previous is not None:
#                 score = int(math.pow(10, streak - 1))
#                 (red, yellow) = (red + score, yellow) if previous else (
#                     red, yellow + score)
#                 # print(streak)
#                 # print(score)
#             streak = 1
#
#         if ((direction == (0, 1) and col == len(board[0]) - 1) or (direction == (1, 0) and row == len(board) - 1)\
#                 or ((direction == (1, 1)) and ((row == len(board) - 1) or (col == len(board[0]) - 1))) \
#                 or ((direction == (-1, 1)) and ((row == 0) or (col == len(board[0]) - 1)))):
#
#             if streak > 1 and previous is not None:
#                 score = int(math.pow(10, streak - 1))
#                 (red, yellow) = (red + score, yellow) if previous else (
#                     red, yellow + score)
#
#         previous = cur_token
#         row += direction[0]
#         col += direction[1]
#
#     # print(red, yellow)
#     # print()
#     return red, yellow, is_win
#
#
# def evaluate_initial_board(board: [[bool | None]]):
#     red = 0
#     yellow = 0
#     directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
#     won = False
#
#     # Loop through the first row + evaluate all lines pass through these points + count the number of points
#     for col in range(len(board[0])):
#         red, yellow, won = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[2], True)
#         if col != 6:
#             red, yellow, _ = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[1])
#         if col != 0:
#             red, yellow, _ = count_consecutive_tokens_in_line(board, (0, col), red, yellow, directions[3])
#
#     for row in range(len(board)):
#         red, yellow, _ = count_consecutive_tokens_in_line(board, (row, 0), red, yellow, directions[0])
#         if row != 0:
#             red, yellow, _ = count_consecutive_tokens_in_line(board, (row, 0), red, yellow, directions[1])
#
#     for row in range(len(board)):
#         if row != 0 and row != 5:
#             red, yellow, _ = count_consecutive_tokens_in_line(board, (row, 6), red, yellow, directions[3])
#
#     return red, yellow,


def is_valid(row, col):
    return 0 <= row < 6 and 0 <= col < 7


def evaluate_initial_board(board: [[bool | None]], player: bool):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # right, down, diag top right, diag top left
    rows, cols = len(board), len(board[0])
    counts = {1: 0, 2: 0, 3: 0, 4: 0}

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player:
                continue
            counts[1] += 1
            for dr, dc in directions:
                # either left, down, diag bot l r is the same player then alr counted
                prev_r, prev_c = row - dr, col - dc
                if is_valid(prev_r, prev_c) and board[prev_r][prev_c] == player:
                    continue

                length = 1
                r, c = row + dr, col + dc
                while is_valid(r, c) and board[r][c] == player:
                    length += 1
                    r += dr
                    c += dc

                if length >= 4:
                    counts[4] += 1
                    return -1  # win
                elif length == 3:
                    counts[3] += 1
                elif length == 2:
                    counts[2] += 1
    points = counts[1] + 10 * counts[2] + 100 * counts[3] + 1000 * counts[4]
    return points
