import math


def count_consecutive_moves_in_line(contents: [bool]):
    red = [0, 0, 0, 0]
    yellow = [0, 0, 0, 0]
    previous = None
    streak = 0
    for index, i in enumerate(contents):
        if i is True:
            red[0] += 1
        if i is False:
            yellow[0] += 1

        if i != previous:
            if streak > 1:
                if previous is True:
                    red[streak - 1] += 1
                elif previous is False:
                    yellow[streak - 1] += 1
            streak = 1
        else:
            if streak < 4:
                streak += 1
        if index == len(contents) - 1 and streak > 1:
            if previous is True:
                red[streak - 1] += 1
            elif previous is False:
                yellow[streak - 1] += 1

        previous = i

    return red, yellow


def calculate_score_in_line(red: [int], yellow: [int]):
    i = 0
    red_score = 0
    yellow_score = 0
    while i < 4:
        multiplier = int(math.pow(10, i))
        red_score += red[i] * multiplier
        yellow_score += yellow[i] * multiplier
        i += 1
    return red_score, yellow_score


MAPPING = {'R': 1, 'Y': 2}


def parse_board(board):
    board = board.split(',')
    for i in range(len(board)):
        ls = list(board[i])
        for j in range(len(ls)):
            if ls[j] == 'r':
                ls[j] = 1
            elif ls[j] == 'y':
                ls[j] = 2
            else:
                ls[j] = 0
        board[i] = ls
    return board


def is_valid(row, col):
    return 0 <= row < 6 and 0 <= col < 7


def initial_board_evaluation(board, player):
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]  # right, down, diag top right, diag top left
    rows, cols = len(board), len(board[0])
    counts = {2: 0, 3: 0, 4: 0}

    for row in range(rows):
        for col in range(cols):
            if board[row][col] != player:
                continue

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
                elif length == 3:
                    counts[3] += 1
                elif length == 2:
                    counts[2] += 1
    return counts
