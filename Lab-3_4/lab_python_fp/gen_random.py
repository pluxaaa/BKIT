import random

def gen_random(num_count, begin, end):
    for x in range(num_count):
        yield random.randrange(begin, end+1)
