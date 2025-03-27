import math

def count_streak_in_line(board: [[bool | None]], start: tuple[int, int], count_streak: [int], direction: tuple[int, int], count_token = False) -> tuple[bool, bool | None]:
    row, col = start
    previous = None
    streak = 1

    while -1 <= row <= len(board) and -1 <= col <= len(board[0]):
        try:
            cur_token = board[row][col]
            # print(cur_token)
            if count_token and cur_token is not None:
                count_streak[0] += 1 if cur_token else -1
            if cur_token == previous and streak < 4:
                streak += 1
            else:
                if streak > 1 and previous is not None:
                    count_streak[streak - 1] += 1 if previous else -1
                    if streak == 4:
                        return True, previous
                streak = 1

            previous = cur_token
            row += direction[0]
            col += direction[1]

        except IndexError:
            if streak > 1 and previous is not None:
                count_streak[streak - 1] += 1 if previous else -1
            return (True, previous) if streak == 4 and previous is not None else (False, None)

    return False, None

def evaluate_initial_board(board: [[bool | None]]) -> tuple[bool, list[int] | bool]:
    streak = [0, 0, 0, 0]
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
    ended = False

    for col in range(len(board[0])):
        ended, winner = count_streak_in_line(board, (0, col), streak, directions[2], True)
        if ended: return ended, winner

    for col in range(len(board[0]) - 1):
        ended, winner = count_streak_in_line(board, (0, col), streak, directions[1])
        if ended: return ended, winner

    for col in range(len(board)):
        ended, winner = count_streak_in_line(board, (0, col + 1), streak, directions[3])
        if ended: return ended, winner

    for row in range(len(board)):
        ended, winner = count_streak_in_line(board, (row, 0), streak, directions[0])
        if ended: return ended, winner

    for row in range(len(board)):
        ended, winner = count_streak_in_line(board, (row + 1, 0), streak, directions[1])
        if ended: return ended, winner

    for row in range(len(board)):
        if row != 0 and row != 5:
            ended, winner = count_streak_in_line(board, (row, 6), streak, directions[3])
            if ended: return ended, winner

    return ended, streak

def update_evaluation_when_add_move(move: tuple[int, int], board: [[bool | None]], turn: bool) -> tuple[bool, list[int] | bool]:
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
    streak = [0, 0, 0, 0]
    ended = False

    start = [(move[0], 0)]
    min_x_y = min(move[0], move[1])
    start.append((move[0] - min_x_y, move[1] - min_x_y))
    start.append((0, move[1]))
    total_x_y = move[0] + move[1]
    start.append((0, total_x_y)) if total_x_y <= 6 else start.append((total_x_y - 6, 6))

    for i in range(len(directions)):
        count_streak_in_line(board, start[i], streak, directions[i],False)

    streak = [-1 * i for i in streak]
    board[move[0]][move[1]] = turn

    for i in range(len(directions)):
        ended, winner = count_streak_in_line(board, start[i], streak, directions[i], False)
        if ended: return ended, winner

    streak[0] = 1 if turn else -1
    return ended, streak

def calculate_evaluation(streak: [int]):
    evaluation = 0
    for i in range(len(streak)):
        evaluation += streak[i] * math.pow(10, i)
    return int(evaluation)








