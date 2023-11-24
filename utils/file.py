from typing import Generator

def write_generator(filename : str, generator : Generator[str, None, None]):
    with open(filename, 'w') as file:
        for sql_statement in generator:
            file.write(f"{sql_statement}\n")