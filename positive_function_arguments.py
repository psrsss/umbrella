"""Positive_function_arguments"""


def validate_arguments(func):
    def wrapper(*args, **kwargs):
        all_args = list(args) + list(kwargs.values())
        for arg in all_args:
            if arg > 0:
                pass
            else:
                raise ValueError(f"Arg {arg} should be > 0")
        return func(*args, **kwargs)
    return wrapper


@validate_arguments
def multiply(a, b):
    print(a * b)


multiply(123, -3)
