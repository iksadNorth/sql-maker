def generator(n : int = 0):
    yield n
    while True:
        n += 1
        yield n