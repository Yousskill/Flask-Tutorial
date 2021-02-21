from functools import wraps


def logged(func):
    def with_logging(*args, **kwargs):
        """does some literature"""
        print(func.__name__ + " was called")
        print(func.__doc__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)
print(f.__doc__)


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        """does some literature"""
        print(func.__name__ + " was called")
        print(func.__doc__ + " was called")
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)
print(f.__doc__)

# logged(f)(1)

