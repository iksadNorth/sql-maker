from typing import Callable

def infinitify(func : Callable):
    while True:
        yield func()