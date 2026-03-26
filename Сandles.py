def solution(candle_number, make_new):
    burnt = candle_number
    remainder = candle_number
    while remainder >= make_new:
        new_candle = remainder // make_new
        burnt += new_candle
        remainder = new_candle + (remainder % make_new)
    return burnt


print(solution(15, 5))
assert solution(5, 2) == 9
assert solution(1, 2) == 1\
assert solution(15, 5) == 18
assert solution(12, 2) == 23
assert solution(6, 4) == 7
assert solution(13, 5) == 16
assert solution(2, 3) == 2
