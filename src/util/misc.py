import itertools
from string import ascii_uppercase


def a2zz():
    """Generator that yield string output "A" to "Z", then "AA" to "ZZ" 

    Yields:
        string: 'A' to 'Z', then 'AA' to 'ZZ'
    """
    for s in range(1, 3, 1):
        for p in itertools.product(ascii_uppercase, repeat=s):
            yield "".join(p)


def Heading(content):
    '''Make a underlined heading
    '''
    return '\n' + content + '\n' + '=' * len(content)
