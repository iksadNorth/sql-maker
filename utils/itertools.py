from typing import Callable

def infinitify(func : Callable):
    while True:
        yield func()

def infinitify_with_args(func):
    def wrapper(*args, **kwargs):
        func_with_args = lambda : func(*args, **kwargs)
        return infinitify(func_with_args)
    return wrapper