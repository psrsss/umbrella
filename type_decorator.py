"""Type decorator"""


def typed(type_):
    def decorator(func):
        def wrapper(*args, **kwargs):
            converted_args = [type_(arg) for arg in args]
            converted_kwargs = {k: type_(v) for k, v in kwargs.items()}
            return func(*converted_args, **converted_kwargs)
        return wrapper
    return decorator


@typed(type_=str)
def add_str(a, b):
    """Adds a and b"""
    print(a + b)


add_str("3", 5)
add_str(5, 5)
add_str('a', 'b')


@typed(type_=int)
def add_int(a, b, c):
    """Sums a, b and c"""
    print(a + b + c)


add_int(5, 6, 7)


@typed(type_=float)
def add_float(a, b, c):
    """Sums a, b and c"""
    print(a + b + c)


add_float(0.1, 0.2, 0.4)
