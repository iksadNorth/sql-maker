from random import randint

def generator(a=0, b=100):
    while True:
        yield randint(a, b)