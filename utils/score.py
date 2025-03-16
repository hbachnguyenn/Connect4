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