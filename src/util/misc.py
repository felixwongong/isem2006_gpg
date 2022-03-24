import itertools
from string import ascii_uppercase


def a2zz():
    for s in range(1, 3, 1):
        for p in itertools.product(ascii_uppercase, repeat=s):
            yield "".join(p)


def Heading(content):
    return '\n' + content + '\n' + '=' * len(content)
