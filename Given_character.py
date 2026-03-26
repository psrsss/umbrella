def solution(remove):
    result = []
    for item in remove:
        if item == '#':
            if result:
                result.pop()
        else:
            result.append(item)
    return "".join(result)


print(solution("a#bc#d"))
print(solution("abc#d##c"))
print(solution("abc##d######"))
print(solution("#######"))
print(solution(""))
assert solution("a#bc#d") == "bd"
assert solution("abc#d##c") == "ac"
assert solution("abc##d######") == ""
assert solution("#######") == ""
assert solution("") == ""
