import itertools
from string import ascii_uppercase


def AddSum(values):
    sum = 0
    for val in values:
        sum += val
    return sum


def a2zz():
    for s in range(1, 3, 1):
        for p in itertools.product(ascii_uppercase, repeat=s):
            yield "".join(p)
