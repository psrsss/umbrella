"""Caching function"""


def cache(func):
    d = {}

    def wrapper(*args):
        if args in d:
            return d[args]
        else:
            result = func(*args)
        d[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)
