from utils.itertools import infinitify
from itertools import islice

def make_tuple(schema : dict):
    keys, values = [], []
    for key, gen in schema.items():
        keys.append(key)
        values.append(next(gen))
    return tuple(keys), tuple(values)

def make_insert_query(table : str, schema : dict):
    keys, values = make_tuple(schema)
    keys = ', '.join(keys)
    keys = f'({keys})'
    return f"""INSERT INTO {table} {keys} VALUES {values};"""

def make_sql_generator(table : str, schema : dict, n : int = 10):
    gen = infinitify(lambda : make_insert_query(table=table, schema=schema))
    gen = islice(gen, n)
    return gen
    