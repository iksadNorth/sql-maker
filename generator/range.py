from random import randint
from utils.itertools import infinitify_with_args

@infinitify_with_args
def generator(a=0, b=100):
    return randint(a, b)