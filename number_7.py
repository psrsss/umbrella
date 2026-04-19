"""Task number 7"""


def f(s, n):
    """Sums my letters"""
    result = s[:n]
    return result + result[:-1][::-1]


S = "abcdefghijklmnopqrstuvwxyz"
print(f(S, 1))
print(f(S, 2))
print(f(S, 3))
print(f(S, 4))
