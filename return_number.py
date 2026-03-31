"""Return number"""


def decorator(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if isinstance(arg, (int, float)):
                pass
            else:
                print("Error! The arg is not number!")
                return None
        return func(*args, **kwargs)
    return wrapper


@decorator
def numbers(a, b):
    print(a, b)


numbers(1, "g")
