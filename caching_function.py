"""Caching function"""


def cache(func):
    "Decorator for cache"""
    d = {}

    def wrapper(*args):
        """Funcrion wrapper"""
        if args in d:
            return d[args]
        result = func(*args)
        d[args] = result
        return result
    return wrapper


@cache
def fibonacci(n):
    """Calculates fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))  # Вывод: 5
print(fibonacci(10))  # Вывод: 55
print(fibonacci(5))  # Вывод: 5 (значение взято из кэша)
