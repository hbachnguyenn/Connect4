import score




a, b = score.count_consecutive_moves_in_line([True, False, True, True, False, True, True])
print(a, b)
red, yellow = score.calculate_score_in_line(a, b)

print(red)
print(yellow)