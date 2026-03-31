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
def add(a, b):
    print(a + b)


add("3", 5)
add(5, 5)
add('a', 'b')


@typed(type_=int)
def add(a, b, с):
    print(a + b + с)


add(5, 6, 7)


@typed(type_=float)
def add(a, b, с):
    print(a + b + с)


add(0.1, 0.2, 0.4)
