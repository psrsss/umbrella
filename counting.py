"""Counting"""


def solution(text):
    new_text = []
    item = text[0]
    num = 0
    for symbol in text:
        if symbol == item:
            num += 1
        else:
            new_text.append(item)
            if num > 1:
                new_text.append(str(num))
            item = symbol
            num = 1
    new_text.append(item)
    if num > 1:
        new_text.append(str(num))
    return "".join(new_text)


print(solution("abeehhhhhccced"))
assert solution("cccbba") == "c3b2a"
assert solution("abeehhhhhccced") == "abe2h5c3ed"
assert solution("aaabbceedd") == "a3b2ce2d2"
assert solution("abcde") == "abcde"
assert solution("aaabbdefffff") == "a3b2def5"
